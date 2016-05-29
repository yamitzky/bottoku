# -*- coding: utf-8 -*-

import pytest

from bottoku.api.slack.renderer import SlackWebhookRenderer
from bottoku.api.slack import template

import helpers


@pytest.fixture()
def webhook_url():
    return helpers.env_or_raise('BOTTOKU_TEST_SLACK_WEBHOOK_URL')


@pytest.fixture()
def receiver_id():
    return helpers.env_or_raise('BOTTOKU_TEST_SLACK_RECEIVER_ID')


def test_slack_webhook_renderer(webhook_url, receiver_id):
    assert SlackWebhookRenderer.api == 'slack_webhook'

    for mention in [True, False]:
        SlackWebhookRenderer(webhook_url, mention).render([
            template.SlackMessage('text message test'),
            template.SlackMessage('text message test', channel="test", username="username_test", icon_emoji=":alien:"),
            template.SlackMessage('text message test', attachments=[template.Attachment(
                fallback='Required plain-text summary of the attachment.',
                color='#36a64f',
                pretext='Optional text that appears above the attachment block',
                author_name='Bobby Tables',
                author_link='https://github.com/yamitzky',
                author_icon='https://yamitzky.com/images/yamitzky.png',
                title='Slack API Documentation',
                title_link='https://api.slack.com/',
                text='Optional text that appears within the attachment',
                fields=[{
                        'title': 'Priority',
                        'value': 'High',
                        'short': False
                }],
                image_url='https://yamitzky.com/images/yamitzky.png',
                thumb_url='https://yamitzky.com/images/yamitzky.png',
                footer='Slack API',
                footer_icon='https://platform.slack-edge.com/img/default_application_icon.png',
                ts=123456789
            )]),
        ], receiver_id)
