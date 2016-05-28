# -*- coding: utf-8 -*-

from collections import namedtuple


class MessageRequest(namedtuple('MessageRequest', 'recipient message')):
    def __new__(cls, receiver_id, message):
        self = super(MessageRequest, cls).__new__(cls, {'id': receiver_id}, message)
        self.receiver_id = receiver_id
        return self


TextMessage = namedtuple('TextMessage', 'text')


class ImageMessage(namedtuple('ImageMessage', 'attachment')):
    def __new__(cls, url):
        self = super(ImageMessage, cls).__new__(cls, {
            'type': 'image',
            'payload': {
                'url': url
            }
        })
        self.url = url
        return self


class ButtonMessage(namedtuple('ButtonMessage', 'attachment')):
    def __new__(cls, text, buttons):
        self = super(ButtonMessage, cls).__new__(cls, {
            'type': 'template',
            'payload': {
                'template_type': 'button',
                'text': text,
                'buttons': buttons
            }
        })
        self.text = text
        self.buttons = buttons
        return self


class Button(namedtuple('Button', 'type title url payload')):
    def __new__(cls, type, title, url=None, payload=None):
        return super(Button, cls).__new__(cls, type, title, url, payload)


class GenericMessage(namedtuple('GenericMessage', 'attachment')):
    def __new__(cls, elements):
        self = super(GenericMessage, cls).__new__(cls, {
            'type': 'template',
            'payload': {
                'template_type': 'generic',
                'elements': elements,
            }
        })
        self.elements = elements
        return self


class Element(namedtuple('Element',
                         'title item_url image_url subtitle buttons')):
    def __new__(cls, title, item_url=None, image_url=None,
                subtitle=None, buttons=None):
        return super(Element, cls).__new__(cls, title, item_url, image_url,
                                           subtitle, buttons)
