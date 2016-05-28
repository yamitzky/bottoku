# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Repository(object):
    """Repository to store receivers' information, typically flag.

    You can set your favorite information for each receivers, i.e. name, age, birth of receivers
    that told by receivers via conversations.
    Bottoku use repository to store flag defined in ``@route`` decorator.

    Currently, BlackholeRepository and DictRepository are implemented as concrete repositories.
    To store to external storage e.g. MySQL, PostgreSQL, redis, memcached, inherit and implement.
    I AM REALLY LOOKING FORWARD TO YOUR AWESOME CONTRIBUTIONS, thanks!
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, repository_id):
        pass


class Record(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, **kwargs):
        pass
