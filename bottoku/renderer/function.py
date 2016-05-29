# -*- coding: utf-8 -*-

from bottoku import Renderer


class FunctionRenderer(Renderer):
    """Renderer which calls function to render"""

    api = 'function'

    def __init__(self, function):
        super(FunctionRenderer, self).__init__()
        self.function = function

    def render(self, message, receiver_id):
        self.function(message, receiver_id)
