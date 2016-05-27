# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Repository(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, repository_id):
        pass


class Record(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, **kwargs):
        pass
