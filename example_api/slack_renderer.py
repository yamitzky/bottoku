# -*- coding: utf-8 -*-

from bottoku.api.slack.renderer import SlackWebhookRenderer
from bottoku.api.slack.template import SlackMessage, Attachment
from bottoku.api.facebook.template import TextMessage, ImageMessage


class FacebookToSlackRenderer(SlackWebhookRenderer):
    def convert(self, messages):
        # convert facebook message format to slack format
        text = []
        attachments = []
        for message in messages:
            if isinstance(message, TextMessage):
                text.append(message.text)
            if isinstance(message, ImageMessage):
                attachments.append(Attachment(image_url=message.url))
        text = '\n'.join(text)

        return [SlackMessage(text=text, attachments=attachments)]
