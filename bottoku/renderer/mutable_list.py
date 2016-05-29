# -*- coding: utf-8 -*-

from bottoku import Renderer


class MutableListRenderer(Renderer):
    """Renderer which appends to list to render"""

    api = 'mutable_list'

    def __init__(self, mutable_list):
        super(MutableListRenderer, self).__init__()
        self.mutable_list = mutable_list

    def render(self, message, receiver_id):
        self.mutable_list.append((message, receiver_id))
