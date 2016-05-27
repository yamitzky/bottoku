# -*- coding: utf-8 -*-

import os

from bottoku import Bot
from bottoku.renderer.stdout import StdoutRenderer
from bottoku.renderer.facebook import FacebookRenderer

import actions
from slack_renderer import MySlackRenderer


class MyBot(Bot):
    def __init__(self, env, receiver_repository):
        super(MyBot, self).__init__(
            env,
            [
                # non-textual message
                actions.unknown,
                actions.media,

                actions.receive_name,
                actions.hello,
                actions.default_text,
            ],
            receiver_repository,
            [
                StdoutRenderer(env),
                FacebookRenderer(env, os.environ['FACEBOOK_TOKEN']),
                MySlackRenderer(env, os.environ['SLACK_URL']),
            ]
        )
