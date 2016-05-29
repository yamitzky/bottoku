# -*- coding: utf-8 -*-

from bottoku import route

import message_types
import views


@route(lambda message, _: message.type == message_types.UNKNOWN)
def unknown(render, message, context):
    render(views.sorry())


@route(lambda message, _: message.type == 'media')
def media(render, message, context):
    render(views.reply_image(message.payload.type))


@route('ASK_NAME',
       lambda message, _: 'hello' in message.payload.text.lower())
def hello(render, message, context):
    render(views.ask_name())


# reset flag
@route('', lambda _, context: context.get('flag') == 'ASK_NAME')
def receive_name(render, message, context):
    name = message.payload.text
    render(views.confirm_name(name))
    context.set(name=name)


@route()
def default_text(render, message, context):
    render(views.default(context.get('name')))
