# -*- coding: utf-8 -*-

from bottoku import route

import re


@route(lambda message, _: re.search('[\s\d+*/()-]+', message.payload))
def calc(render, message, context):
    reply = eval(message.payload)
    render(reply)


@route(lambda message, _: message.payload == '42')
def fortytwo(render, message, context):
    render('the Answer to the Ultimate Question of Life, '
           'the Universe, and Everything')


@route()
def echo(render, message, context):
    reply = message.payload * 3
    render(reply)
