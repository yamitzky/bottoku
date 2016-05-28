# -*- coding: utf-8 -*-

from bottoku import Renderer


class FunctionRenderer(Renderer):
    """"""

    api = 'function'

    def __init__(self, function):
        self.function = function

    def render(self, message, receiver_id):
        self.function(message, receiver_id)
