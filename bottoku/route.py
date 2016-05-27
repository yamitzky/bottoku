# -*- coding: utf-8 -*-

import functools


def route(scene=None, cond_func=None):
    if hasattr(scene, '__call__'):  # route(lambda m, c: result)
        cond_func = scene
        scene = None

    def receive_func(func):
        @functools.wraps(func)
        def wrapper(message, context):
            if cond_func is None or cond_func(message, context):
                return True, func, scene
            return False, None, None
        return wrapper
    return receive_func
