# -*- coding: utf-8 -*-

import collections


SlackMessage = collections.namedtuple('SlackMessage', ['text', 'attacments'])


_attachment_fields = [
    'fallback', 'color', 'pretext',
    'author_name', 'author_link', 'author_icon',
    'title', 'title_link', 'text', 'fields', 'image_url', 'thumb_url']


class Attachment(collections.namedtuple('Attachment', _attachment_fields)):
    def __new__(cls, **kwargs):
        default = {f: None for f in _attachment_fields}
        default.update(kwargs)
        return super(cls, Attachment).__new__(
            cls, **default)
