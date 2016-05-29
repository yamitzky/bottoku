# -*- coding: utf-8 -*-

from bottoku import IncomingMessage, Environment
from bottoku.repository.dict_repository import DictRepository

from bot import MyBot
from input_payload import TextPayload, MediaPayload
import message_types


cache = DictRepository()  # Do not use with AWS Lambda


def facebook_handler(event, context):
    env = Environment(api='facebook')

    for entry in event['entry']:
        for message in entry['messaging']:
            receiver_id = message['sender']['id']

            if message.get('message', {}).get('text'):
                # text message in facebook
                msg = IncomingMessage(
                    type=message_types.TEXT,
                    payload=TextPayload(message['message']['text']),
                )

            elif message.get('message', {}).get('attachments', []):
                # message w/ media
                attachment = message['message']['attachments'][0]
                msg = IncomingMessage(
                    type='media',  # your favorite type name
                    payload=MediaPayload(
                        type=attachment['type'],
                        url=attachment['payload']['url']
                    )
                )

            else:
                msg = IncomingMessage(
                    type=message_types.UNKNOWN,
                    payload=None
                )

            # WARNING: not good, use lambda's invokeFunction
            # to reply async and return response immediately
            MyBot(env, cache).reply(msg, receiver_id)


if __name__ == '__main__':
    import sys
    from config import config
    if len(sys.argv) >= 2:
        facebook_handler({
            'object': 'page',
            'entry': [{
                'id': '',
                'time': 1457764198246,
                'messaging': [{
                    'sender': {'id': config['BOTTOKU_TEST_FACEBOOK_RECEIVER_ID']},
                    'recipient': {'id': 'PAGE_ID'},
                    'timestamp': 1457764197627,
                    'message': {
                        'mid': 'mid.1457764197618:41d102a3e1ae206a38',
                        'seq': 73,
                        'text': sys.argv[1]
                    }
                }]
            }]
        }, None)
    else:
        print('Usage: python example_api/facebook_handler.py "Your message"')
