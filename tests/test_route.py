# -*- coding: utf-8 -*-
from bottoku import route


def test_route_with_no_args():
    @route()
    def func(message, context):
        return message, context

    match, action, flag = func(None, None)
    assert match  # always matches
    assert action('arg1', 'arg2') == ('arg1', 'arg2')  # callable as original function
    assert flag is None


def test_route_with_flag():
    @route('flag')
    def func(message, context):
        return message, context

    match, action, flag = func(None, None)
    assert match  # always matches
    assert action('arg1', 'arg2') == ('arg1', 'arg2')  # callable as original func
    assert flag == 'flag'


def test_route_with_condition():
    @route(lambda message, context: message and context)
    def func(message, context):
        return message, context

    # when matched
    match, action, flag = func(True, True)
    assert match
    assert action('arg1', 'arg2') == ('arg1', 'arg2')
    assert flag is None

    # when not matched
    match, action, flag = func(True, False)
    assert not match
    assert action is None
    assert flag is None  # flag wont be set if not matched

    match, action, flag = func(False, True)
    assert not match
    assert action is None
    assert flag is None  # flag wont be set if not matched


def test_route_with_flag_and_condition():
    @route('flag', lambda message, context: message and context)
    def func(message, context):
        return message, context

    # when matched
    match, action, flag = func(True, True)
    assert match
    assert action('arg1', 'arg2') == ('arg1', 'arg2')
    assert flag == 'flag'

    # when not matched
    match, action, flag = func(True, False)
    assert not match
    assert action is None
    assert flag is None

    match, action, flag = func(False, True)
    assert not match
    assert action is None
    assert flag is None
