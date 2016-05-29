# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Renderer(object):
    """Abstract class of Renderer, i.e. API client.

    In Bottoku, API Client is Renderer. Currently, implemented renderers are Facebook, Slack,
    and Line. For other APIs, inherit Renderer class and implement it.
    I AM REALLY LOOKING FORWARD TO YOUR AWESOME CONTRIBUTIONS, thanks!

    To implement concrete renderers, override ``api`` property and ``render`` function.

    :param basestring api:
    """

    __metaclass__ = ABCMeta

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

    @abstractmethod
    def render(self, messages, receiver_id):
        """Send request to message API.

        When implementing render, do not forget to call ``convert`` method in this method.

        :param list messages: messages to send
        :param receiver_id: id to send messages to
        """
