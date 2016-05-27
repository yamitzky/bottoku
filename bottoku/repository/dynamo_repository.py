# -*- coding: utf-8 -*-

from bottoku import Repository, Record


class DynamoRepository(Repository):
    def __init__(self, table, id_col):
        self.table = table
        self.id_col = id_col

    def get(self, receiver_id):
        return DynamoRecord(self.table, self.id_col, receiver_id)


class DynamoRecord(dict, Record):
    def __init__(self, table, id_col, id):
        self.table = table
        self.id_col = id_col
        self.id = id
        self._item = None

    def fetch(self):
        if self._item is None:
            key = {self.id_col: self.id}
            response = self.table.get_item(key=key)
            self._item = response.get('Item')
        return self._item

    def get(self, field, default=None):
        item = self.fetch()
        if item is None:
            return
        return item.get(field, default)

    def set(self, **kwargs):
        kwargs = {k: v for k, v in kwargs.items()}
        kwargs.update({self.id_col: self.id})
        self.table.put_item(Item=kwargs)
