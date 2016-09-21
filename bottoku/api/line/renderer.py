# -*- coding: utf-8 -*-

from requests import Request

from bottoku import NetworkRenderer
from bottoku.api.line import constant
from bottoku.api.line.template import MultipleMessagesRequest


class LineRenderer(NetworkRenderer):
    api = 'line'

    def __init__(self, channel_id, channel_secret, channel_mid):
        super(LineRenderer, self).__init__()
        self.channel_id = channel_id
        self.channel_secret = channel_secret
        self.channel_mid = channel_mid

    def json_bodies(self, messages, receiver_id):
        return [MultipleMessagesRequest([receiver_id], messages)]

    def prepared_requests(self, jsons):
        return [
            Request(
                'POST',
                'https://{}/v1/events'.format(constant.API_HOST_TRIAL),
                json=body,
                headers={
                    'X-Line-ChannelID': self.channel_id,
                    'X-Line-ChannelSecret': self.channel_secret,
                    'X-Line-Trusted-User-With-ACL': self.channel_mid
                }
            ).prepare()
            for body in jsons]
