# -*- coding: utf-8 -*-
import collections


InputMessage = collections.namedtuple('Message', ['type', 'payload'])


class Environment(object):
    def __init__(self, api, env=None):
        self.api = api
        self.env = env
