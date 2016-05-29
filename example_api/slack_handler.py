# -*- coding: utf-8 -*-

from bottoku import IncomingMessage, Environment
from bottoku.repository.dict_repository import DictRepository

from bot import MyBot
from input_payload import TextPayload
import message_types


cache = DictRepository()  # Do not use with AWS Lambda


def slack_handler(event, context):
    env = Environment(api='slack_webhook')

    msg = IncomingMessage(
        type=message_types.TEXT,
        payload=TextPayload(event['text']),
    )
    receiver_id = event['user_name']
    MyBot(env, cache).reply(msg, receiver_id)


if __name__ == '__main__':
    import sys
    from config import config

    if len(sys.argv) >= 2:
        slack_handler({
            'token': 'OQEKlq1RzjoQKISXSImKSQIr',
            'team_id': 'T0001',
            'team_domain': 'example',
            'channel_id': 'C2147483705',
            'channel_name': 'test',
            'timestamp': '1355517523.000005',
            'user_id': 'U2147483697',
            'user_name': config['BOTTOKU_TEST_SLACK_RECEIVER_ID'],
            'text': 'googlebot: {}'.format(sys.argv[1]),
            'trigger_word': 'googlebot:'.format(),
        }, None)
    else:
        print('Usage: python example_api/slack_handler.py "Your message"')
