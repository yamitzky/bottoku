# -*- coding: utf-8 -*-

from bottoku import InputMessage, Environment, types
from bottoku.repository.dict_repository import DictRepository

from bot import MyBot
from input_payload import TextPayload, MediaPayload


cache = DictRepository()  # Do not use with AWS Lambda


def facebook_handler(event, context):
    env = Environment(api='facebook')

    for entry in event['entry']:
        for message in entry['messaging']:
            receiver_id = message['sender']['id']

            if message.get('message', {}).get('text'):
                # text message in facebook
                msg = InputMessage(
                    type=types.TEXT,
                    payload=TextPayload(message['message']['text']),
                )

            elif message.get('message', {}).get('attachments', []):
                # message w/ media
                attachment = message['message']['attachments'][0]
                msg = InputMessage(
                    type='media',  # your favorite type name
                    payload=MediaPayload(
                        type=attachment['type'],
                        url=attachment['payload']['url']
                    )
                )

            else:
                msg = InputMessage(
                    type=types.UNKNOWN,
                    payload=None
                )

            # WARNING: not good, use lambda's invokeFunction
            # to reply async and return response immediately
            MyBot(env, cache).reply(msg, receiver_id)
