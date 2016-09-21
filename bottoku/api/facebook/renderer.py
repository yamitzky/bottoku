# -*- coding: utf-8 -*-

from requests import Request

from bottoku import NetworkRenderer
from bottoku.api.facebook.template import MessageRequest


class FacebookRenderer(NetworkRenderer):

    api = 'facebook'

    def __init__(self, token):
        super(FacebookRenderer, self).__init__()
        self.token = token

    def json_bodies(self, messages, receiver_id):
        return [MessageRequest(receiver_id, message)
                for message in messages]

    def prepared_requests(self, jsons):
        return [Request('POST', 'https://graph.facebook.com/v2.6/me/messages',
                        params={'access_token': self.token},
                        json=body).prepare()
                for body in jsons]
