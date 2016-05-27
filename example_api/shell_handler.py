# -*- coding: utf-8 -*-

from bottoku import InputMessage, Environment, types
from bottoku.repository.dict_repository import DictRepository

from bot import MyBot
from input_payload import TextPayload


cache = DictRepository()


def shell_handler(text):
    msg = InputMessage(
        type=types.TEXT,
        payload=TextPayload(text),
    )
    env = Environment(api='stdout')

    MyBot(env, cache).reply(msg, None)


if __name__ == '__main__':
    # for test purpose
    while True:
        print('input...')
        shell_handler(raw_input())
