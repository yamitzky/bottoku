# -*- coding: utf-8 -*-

import requests

from bottoku import Renderer
from bottoku.api.line import constant
from bottoku.api.line.template import MultipleMessagesRequest


class LineRenderer(Renderer):

    api = 'line'

    def __init__(self, channel_id, channel_secret, channel_mid):
        super(LineRenderer, self).__init__()
        self.channel_id = channel_id
        self.channel_secret = channel_secret
        self.channel_mid = channel_mid

    def render(self, messages, receiver_id):
        response = requests.post(
            'https://{}/v1/events'.format(constant.API_HOST_TRIAL),
            json=MultipleMessagesRequest(
                [receiver_id], self.convert(messages)
            ),
            headers={
                'X-Line-ChannelID': self.channel_id,
                'X-Line-ChannelSecret': self.channel_secret,
                'X-Line-Trusted-User-With-ACL': self.channel_mid
            }
        )
        print(response.text)
        response.raise_for_status()
