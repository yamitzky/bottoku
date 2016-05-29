# -*- coding: utf-8 -*-

import os


def env_or_raise(key):
    value = os.environ.get(key)
    if value is not None:
        return value
    else:
        raise Exception(('Define "{0}" in your environment\n'
                         '$ export {0}="value_for_your_env"').format(key))


