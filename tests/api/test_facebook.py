# -*- coding: utf-8 -*-

import pytest

from bottoku.api.facebook import template
from bottoku.api.facebook.renderer import FacebookRenderer
import helpers


@pytest.fixture()
def token():
    return helpers.env_or_raise('BOTTOKU_TEST_FACEBOOK_TOKEN')


@pytest.fixture()
def receiver_id():
    return helpers.env_or_raise('BOTTOKU_TEST_FACEBOOK_RECEIVER_ID')


def test_facebook_renderer(token, receiver_id):
    renderer = FacebookRenderer(token)

    buttons = [
        template.WebURLButton(title='title_web_url', url='https://yamitzky.com'),
        template.PostbackButton(title='title_postback', payload='POST_BACK'),
    ]
    elements = [
        template.Element(title='title and image_url', image_url='https://yamitzky.com/images/yamitzky.png'),
        template.Element(title='title and subtitle', subtitle='subtitle only'),
        template.Element(title='title and buttons', buttons=buttons),
        template.Element(title='title generic',
                         item_url='https://yamitzky.com',
                         image_url='https://yamitzky.com/images/yamitzky.png',
                         subtitle='test subtitle',
                         buttons=buttons)
    ]

    # sequential messages
    renderer.render([
        template.TextMessage('hello'),
        template.ImageMessage('https://yamitzky.com/images/yamitzky.png'),
        template.ButtonMessage('buttons test', buttons),
        template.GenericMessage(elements),
    ], receiver_id)

    # no assertion, called successfully!
