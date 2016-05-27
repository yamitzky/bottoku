# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Renderer(object):

    __metaclass__ = ABCMeta

    def __init__(self, env):
        self.env = env

    @classmethod
    def convert(cls, messages):
        return messages

    @abstractmethod
    def render(self, messages, receiver_id):
        pass
