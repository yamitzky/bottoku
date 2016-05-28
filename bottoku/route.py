# -*- coding: utf-8 -*-

import functools


def route(flag=None, route_func=None):
    """Decorator to route messages by decorates action functions.

    When `route_func` returns True, decorated function will be fired.
    After firing and all operations of the function are done, `flag` will be set to receiver.

    Flag is used to distinguish receivers' conversational status, "scene."
    See 'example_api/actions.py' for further usages.

    :param basestring flag: (optional) receiver's flag to be saved after firing
    :param function route_func: (optional) function to check if decorated function should be fired

    Usage::

        >>> # Matches ALL messages and fire decorated function always.
        >>> @route()
        >>> def answer(message, context):
        >>>     pass

        >>> # Matches ALL messages and fire decorated function always.
        >>> # After firing, flag will be set to receiver.
        >>> @route('flag_for_conversation')
        >>> def start_conversation(message, context):
        >>>     pass

        >>> # Matches when route_func returns True, and fire decorated function.
        >>> @route(lambda message, context: 'hello' in message.text)
        >>> def reply_to_hello(message, context):
        >>>     pass

        >>> # Matches when route_func returns True, and fire decorated function.
        >>> # After firing, flag will be set to receiver.
        >>> @route('flag_for_conversation',
        >>>        lambda message, context: "let's start a game" == message.text)
        >>> def start_game(message, context):
        >>>     pass
    """
    if hasattr(flag, '__call__'):  # route(lambda m, c: result)
        route_func = flag
        flag = None

    def receive_func(func):
        @functools.wraps(func)
        def wrapper(message, context):
            """
            :param message: type is the 1st arg of Bot#reply, typically dict.
            :param dict context: response of `receiver_repository.get`
            :return tuple: (matched(bool), decorated function, flag(basestring))
            """
            if route_func is None or route_func(message, context):
                return True, func, flag
            return False, None, None
        return wrapper
    return receive_func
