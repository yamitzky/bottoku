# -*- coding: utf-8 -*-

import pytest

import helpers
from bottoku.api.line.renderer import LineRenderer
from bottoku.api.line import template


@pytest.fixture()
def channel_id():
    return helpers.env_or_raise('BOTTOKU_TEST_LINE_CHANNEL_ID')


@pytest.fixture()
def channel_secret():
    return helpers.env_or_raise('BOTTOKU_TEST_LINE_CHANNEL_SECRET')


@pytest.fixture()
def channel_mid():
    return helpers.env_or_raise('BOTTOKU_TEST_LINE_CHANNEL_MID')


@pytest.fixture()
def receiver_id():
    return helpers.env_or_raise('BOTTOKU_TEST_LINE_RECEIVER_ID')


def test_line_renderer(channel_id, channel_secret, channel_mid, receiver_id):
    renderer = LineRenderer(channel_id, channel_secret, channel_mid)
    renderer.render([
        template.TextMessage(text='sample text'),
        template.ImageMessage(original_content_url='https://yamitzky.com/images/yamitzky.png',
                              preview_image_url='https://yamitzky.com/images/yamitzky.png'),
        # TODO: other type of messages
    ], receiver_id)
