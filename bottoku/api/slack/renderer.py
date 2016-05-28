# -*- coding: utf-8 -*-

import requests

from bottoku.renderer.renderer import Renderer


class SlackRenderer(Renderer):

    api = 'slack'

    def __init__(self, env, url):
        super(SlackRenderer, self).__init__(env)
        self.url = url

    def render(self, messages, receiver_id):
        for message in self.convert(messages):
            requests.post(self.url, json=message)
