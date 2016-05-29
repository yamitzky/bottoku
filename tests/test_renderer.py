# -*- coding: utf-8 -*-
from bottoku import Renderer
from bottoku.renderer.function import FunctionRenderer
from bottoku.renderer.mutable_list import MutableListRenderer


def test_abstract_renderer():
    # default implementation is identity function
    assert Renderer.convert(['m1', 'm2', 'm3']) == ['m1', 'm2', 'm3']


def test_function_renderer():
    assert FunctionRenderer.api == 'function'

    def closure(message, receiver_id):
        assert message == 'message'
        assert receiver_id == 'receiver_id'

    FunctionRenderer(closure).render('message', 'receiver_id')


def test_mutable_list_renderer():
    assert MutableListRenderer.api == 'mutable_list'

    mutable_list = []
    renderer = MutableListRenderer(mutable_list)
    renderer.render('message1', 'receiver1')
    renderer.render('message2', 'receiver2')

    assert mutable_list[0] == ('message1', 'receiver1')
    assert mutable_list[1] == ('message2', 'receiver2')
