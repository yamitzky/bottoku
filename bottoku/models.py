# -*- coding: utf-8 -*-


class IncomingMessage(object):
    """Plain object represents incoming message.

    Instantiate and pass to ``Bot#reply`` method.

    In case of you want to analyze incoming messages further(ex: PoS tagging, analyzing via CNNs),
    make a super class and analyze in ``__init__`` function.

    :param payload: incoming messages' contents, typically dict but not restricted.
    :param basestring type: (optional) message type (ex: text, image, emoji, ...)
    """
    def __init__(self, payload, type=None):
        self.payload = payload
        self.type = type


class Environment(object):
    """Plain object represents execution environment including API and development environment.

    The param ``api`` is very important in this framework. This is used to determine which renderer
    to use. The value is defined in each renderer, e.g. 'facebook', 'slack', 'line', or your customized
    renderer's name.

    The param ``env`` is defined for convention and will not be used, but you can use it.

    :param basestring api: API name defined in renderers
    :param basestring env: development environment like 'dev' or 'prod'
    """

    def __init__(self, api, env=None):
        self.api = api
        self.env = env
