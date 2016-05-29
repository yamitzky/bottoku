# -*- coding: utf-8 -*-

from bottoku import Bot
from bottoku.renderer.stdout import StdoutRenderer
from bottoku.api.facebook.renderer import FacebookRenderer

import actions
from config import config
from slack_renderer import FacebookToSlackRenderer


class MyBot(Bot):
    def __init__(self, env, receiver_repository):
        renderers = [StdoutRenderer()]
        if 'BOTTOKU_TEST_FACEBOOK_TOKEN' in config:
            token = config['BOTTOKU_TEST_FACEBOOK_TOKEN']
            renderers.append(FacebookRenderer(token))
        if 'BOTTOKU_TEST_SLACK_WEBHOOK_URL' in config:
            url = config['BOTTOKU_TEST_SLACK_WEBHOOK_URL']
            renderers.append(FacebookToSlackRenderer(url))

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
            renderers
        )
