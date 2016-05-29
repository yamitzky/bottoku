# -*- coding: utf-8 -*-
import logging

import requests

from bottoku import Renderer
from bottoku.api.facebook.template import MessageRequest


class FacebookRenderer(Renderer):

    api = 'facebook'

    def __init__(self, token):
        super(FacebookRenderer, self).__init__()
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
            if not response.ok:
                logging.warn('Failed status {}: {}'.format(response.status_code, response.text))
            response.raise_for_status()
