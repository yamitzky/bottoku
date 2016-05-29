# -*- coding: utf-8 -*-

import collections


_fields = ['text', 'attachments', 'channel', 'username', 'icon_emoji']


class SlackMessage(collections.namedtuple('SlackMessage', _fields)):
    def __new__(cls, text, attachments=None, channel=None, username=None, icon_emoji=None):
        return super(SlackMessage, cls).__new__(
            cls, text, attachments, channel, username, icon_emoji)

    def add_mention(self, to):
        """Add "@to :" to text and returns copied object"""
        text = '@{}: {}'.format(to, self.text)
        return self._replace(text = text)

    def replace_text(self, text):
        """Replaces text and returns copied object"""
        return self._replace(text=text)


_attachment_fields = [
    'fallback', 'color', 'pretext',
    'author_name', 'author_link', 'author_icon',
    'title', 'title_link', 'text', 'fields', 'image_url', 'thumb_url', 'footer', 'footer_icon', 'ts']


class Attachment(collections.namedtuple('Attachment', _attachment_fields)):
    def __new__(cls, **kwargs):
        default = {f: None for f in _attachment_fields}
        default.update(kwargs)
        return super(cls, Attachment).__new__(
            cls, **default)
