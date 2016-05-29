# -*- coding: utf-8 -*-

from bottoku.repository.dict_repository import DictRepository
from bottoku.repository.blackhole_repository import BlackholeRepository


def test_dict_repository():
    repo = DictRepository()
    record = repo.get('receiver_id')
    assert len(record) == 0

    record.set(key='value')
    assert record['key'] == 'value'

    record.set(key2='value2', key3='value3')
    assert record['key2'] == 'value2'
    assert record['key3'] == 'value3'

    # check if set and  cached
    record = repo.get('receiver_id')
    assert record['key'] == 'value'
    assert record['key2'] == 'value2'
    assert record['key3'] == 'value3'

    # check if no side effect to other receivers
    record = repo.get('receiver_id_2')
    assert len(record) == 0


def test_blackhole_repository():
    repo = BlackholeRepository()
    record = repo.get('receiver_id')
    assert record is None
