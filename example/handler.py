# -*- coding: utf-8 -*-

from bottoku import Bot, IncomingMessage, Environment
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
            StdoutRenderer()
        )


def shell_handler(text):
    msg = IncomingMessage(
        type='TEXT',
        payload=text,
    )

    env = Environment(api='stdout')
    receiver_id = None

    bot = MyBot(env)
    bot.reply(msg, receiver_id)


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        shell_handler(sys.argv[1].decode('utf-8'))
    else:
        print('Usage: python example/handler.py "Your message"')
