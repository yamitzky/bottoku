# -*- coding: utf-8 -*-

import collections

from bottoku.api.line import constant


# TODO: Implement Rich message

class MultipleMessagesRequest(collections.namedtuple('MultipleMessageRequest',
                                                     'to toChannel eventType content')):
    def __new__(cls, to, messages):
        self = super(MultipleMessagesRequest, cls).__new__(
            cls, to, constant.OUT_TO_CHANNEL, constant.OUT_EVENT_TYPE_MULTIPLE_MESSAGE, {
                'messages': messages
            })
        self.messages = messages
        return self


class TextMessage(collections.namedtuple('TextMessage', 'contentType toType text')):
    def __new__(cls, text):
        return super(TextMessage, cls).__new__(cls, constant.CONTENT_TYPE_TEXT, 1, text)


class ImageMessage(collections.namedtuple('ImageMessage',
                                          'contentType toType originalContentUrl previewImageUrl')):
    def __new__(cls, original_content_url, preview_image_url):
        return super(ImageMessage, cls).__new__(
            cls, constant.CONTENT_TYPE_IMAGE, 1, original_content_url, preview_image_url)


class VideoMessage(collections.namedtuple('VideoMessage', 'contentType toType originalContentUrl previewImageUrl')):
    def __new__(cls, original_content_url, preview_image_url):
        return super(VideoMessage, cls).__new__(
            cls, constant.CONTENT_TYPE_VIDEO, 1, original_content_url, preview_image_url)


class AudioMessage(collections.namedtuple('AudioMessage', 'contentType toType originalContentUrl contentMetadata')):
    def __new__(cls, original_content_url, audlen):
        self = super(AudioMessage, cls).__new__(
            cls, constant.CONTENT_TYPE_AUDIO, 1, original_content_url, {
                'AUDLEN': audlen
            })
        self.audlen = audlen
        return self


class LocationMessage(collections.namedtuple('AudioMessage', 'contentType toType text location')):
    def __new__(cls, text, title, latitude, longitude):
        self = super(LocationMessage, cls).__new__(cls, constant.CONTENT_TYPE_LOCATION, 1, text, {
            'title': title,
            'latitude': latitude,
            'longitude': longitude,
        })
        self.title = title
        self.latitude = latitude
        self.longitude = longitude


class StickerMessage(collections.namedtuple('StickerMessage', 'contentType toType contentMetadata')):
    def __new__(cls, stkid, stkpkgid, stkver=None):
        self = super(StickerMessage, cls).__new__(cls, constant.CONTENT_TYPE_STICKER, 1, {
            'STKID': stkid,
            'STKPKGID': stkpkgid,
            'STKVER': stkver
        })
        self.stkid = stkid
        self.stkpkgid = stkpkgid
        self.stkver = stkver
