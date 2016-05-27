# -*- coding: utf-8 -*-

from bottoku import InputMessage, Environment, types
from bottoku.repository.dict_repository import DictRepository

from bot import MyBot
from input_payload import TextPayload


cache = DictRepository()  # Do not use with AWS Lambda


def slack_handler(event, context):
    env = Environment(api='slack')

    msg = InputMessage(
        type=types.TEXT,
        payload=TextPayload(event['text']),
    )
    receiver_id = event['user_name']
    MyBot(env, cache).reply(msg, receiver_id)
