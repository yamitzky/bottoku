# -*- coding: utf-8 -*-

from bottoku import Repository, Record


class DictRepository(Repository):
    """Repository to store on memory via Python's ``dict``"""

    def __init__(self):
        import collections
        self.cache = collections.defaultdict(DictRecord)

    def get(self, receiver_id):
        return self.cache[receiver_id]


class DictRecord(dict, Record):
    def set(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value
