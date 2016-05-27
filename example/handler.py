# -*- coding: utf-8 -*-

from bottoku import Bot, InputMessage, Environment, types
from bottoku.repository.blackhole_repository import BlackholeRepository
from bottoku.renderer.stdout import StdoutRenderer

import actions


class MyBot(Bot):
    def __init__(self, env):
        super(MyBot, self).__init__(
            env,
            [
                actions.fortytwo,
                actions.calc,
                actions.echo,
            ],
            BlackholeRepository(),
            StdoutRenderer(env)
        )


def shell_handler(text):
    msg = InputMessage(
        type=types.TEXT,
        payload=text,
    )

    env = Environment(api='stdout')
    receiver_id = None

    bot = MyBot(env)
    bot.reply(msg, receiver_id)


if __name__ == '__main__':
    import sys
    shell_handler(sys.argv[1].decode('utf-8'))
