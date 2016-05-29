# -*- coding: utf-8 -*-

from bottoku import Repository


class BlackholeRepository(Repository):
    """Repository to store nothing"""

    def __init__(self):
        pass

    def get(self, repository_id):
        """Always returns None"""
        pass
