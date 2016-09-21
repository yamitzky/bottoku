# -*- coding: utf-8 -*-
import logging
from abc import ABCMeta, abstractmethod
from requests import Session


class Renderer(object):
    """Abstract class of Renderer, i.e. API client.

    In Bottoku, API Client is Renderer. Currently, implemented renderers are Facebook, Slack,
    and Line. For other APIs, inherit Renderer class and implement it.
    I AM REALLY LOOKING FORWARD TO YOUR AWESOME CONTRIBUTIONS, thanks!

    To implement concrete renderers, override ``api`` property and ``render`` function.

    :param basestring api:
    """

    api = None  # name of API, e.g. 'facebook', 'slack', 'line'
    """:type: basestring"""

    @classmethod
    def convert(cls, messages):
        """Convert received messages to conform to API request.

        Initially this method is an identity function, returns received messages.
        Response of this function will be used in ``render`` function.

        When you want your project to respond to multiple APIs, you will make view functions to
        return common intermediate objects. However, these objects cannot be sent to API without
        converting to ``dict``(or namedtuple in ``requests`` library). In these cases, you can
        inherit pre-defined renderers, e.g. FacebookRenderer, and override ``convert`` to conform
        to APIs, e.g. Facebook.

        :param list messages: messages to convert
        :return: messages to conform to API request
        """
        return messages

    def render(self, messages, receiver_id):
        """Send request to message API.

        When implementing render, do not forget to call ``convert`` method in this method.

        :param list messages: messages to send
        :param receiver_id: id to send messages to
        """


class NetworkRenderer(Renderer):

    __metaclass__ = ABCMeta

    @abstractmethod
    def json_bodies(self, messages, receiver_id):
        """Build json bodies to be passed as json.

        Returned type may be list of any types that can be serialized by requests.

        :param list messages: messages to send
        :param receiver_id: id to send messages to
        :rtype: list
        """

    @abstractmethod
    def prepared_requests(self, jsons):
        """Build requests's PreparedRequest instances.

        :param list jsons: message bodies to be serialized and sent
        :rtype: list[requests.PreparedRequest]
        """

    def render(self, messages, receiver_id):
        responses = []
        with Session() as session:
            converted = self.convert(messages)
            jsons = self.json_bodies(converted, receiver_id)
            for req in self.prepared_requests(jsons):
                response = session.send(req)
                responses.append(response)

        for response in responses:
            if not response.ok:
                logging.warn('Failed status {}: {}'.format(response.status_code, response.text))
            response.raise_for_status()
