# -*- coding: utf-8 -*-

from requests import Request

from bottoku import NetworkRenderer


class SlackWebhookRenderer(NetworkRenderer):

    api = 'slack_webhook'

    def __init__(self, webhook_url, mention=False):
        super(SlackWebhookRenderer, self).__init__()
        self.webhook_url = webhook_url
        self.mention = mention

    def json_bodies(self, messages, receiver_id):
        bodies = []
        for message in messages:
            if self.mention:
                message = message.add_mention(receiver_id)
            bodies.append(message)
        return bodies

    def prepared_requests(self, jsons):
        return [Request('POST', self.webhook_url, json=body).prepare()
                for body in jsons]
