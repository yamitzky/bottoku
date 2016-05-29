import os


config = {}
for env in ['BOTTOKU_TEST_FACEBOOK_TOKEN',
            'BOTTOKU_TEST_FACEBOOK_RECEIVER_ID',
            'BOTTOKU_TEST_SLACK_WEBHOOK_URL',
            'BOTTOKU_TEST_SLACK_RECEIVER_ID']:
    if env in os.environ:
        config[env] = os.environ[env]
    else:
        raise Exception(('Define environment "{0}"'
                         '$ export {0}="blah blah blah"').format(env))
