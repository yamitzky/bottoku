# -*- coding: utf-8 -*-

import collections

# define your favorite common payload types, and use them from every handlers

TextPayload = collections.namedtuple('TextPayload', ['text'])

MediaPayload = collections.namedtuple('MediaPayload', ['type', 'url'])
