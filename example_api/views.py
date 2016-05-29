# -*- coding: utf-8 -*-

# this example uses facebook template as common output format.
# but you do not have to do it.
from bottoku.api.facebook.template import TextMessage, ImageMessage


def sorry():
    return [TextMessage(
        'sorry, i cant understand what you mean...\n'
        'try to say "hello"'
    )]


def reply_image(media_type):
    return [
        TextMessage(
            ('good {}, but i cant see it. '
             "btw, i give you my dog's photo.").format(media_type),
        ),
        ImageMessage('https://s3.amazonaws.com/yamitzky.com/atom.png')
    ]


def ask_name():
    return [TextMessage("hi! what's your name?")]


def confirm_name(name):
    return [TextMessage(
        'oh, your name is {}? Great!'.format(name)
    )]


def default(name=None):
    response = ''
    if name:
        response += 'hi {}, '.format(name)
    response += 'try to say "hello"'

    return [TextMessage(response)]
