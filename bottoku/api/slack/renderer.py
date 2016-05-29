# -*- coding: utf-8 -*-
import logging

import requests

from bottoku import Renderer


class SlackWebhookRenderer(Renderer):

    api = 'slack_webhook'

    def __init__(self, webhook_url, mention=False):
        super(SlackWebhookRenderer, self).__init__()
        self.webhook_url = webhook_url
        self.mention = mention

    def render(self, messages, receiver_id):
        responses = []
        for message in self.convert(messages):
            if self.mention:
                message = message.add_mention(receiver_id)
            response = requests.post(self.webhook_url, json=message)
            responses.append(response)
            if not response.ok:
                logging.warn('Failed status {}: {}'.format(response.status_code, response.text))

        for response in responses:
            response.raise_for_status()
