# -*- coding: utf-8 -*-

from bottoku.renderer.slack import SlackRenderer
from bottoku.output.facebook import TextMessage, ImageMessage
from bottoku.output.slack import SlackMessage, Attachment


class MySlackRenderer(SlackRenderer):
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
