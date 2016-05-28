# -*- coding: utf-8 -*-

import requests

from bottoku.renderer.renderer import Renderer
from bottoku.output.facebook import MessageRequest


class FacebookRenderer(Renderer):

    api = 'facebook'

    def __init__(self, env, token):
        super(FacebookRenderer, self).__init__(env)
        self.env = env
        self.token = token

    def render(self, messages, receiver_id):
        responses = []
        for message in self.convert(messages):
            response = requests.post(
                'https://graph.facebook.com/v2.6/me/messages',
                params={'access_token': self.token},
                json=MessageRequest(receiver_id, message))
            responses.append(response)

        for response in responses:
            response.raise_for_status()
