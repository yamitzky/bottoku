# -*- coding: utf-8 -*-
import logging


class Bot(object):
    """Main application class.

    Simple usage is to instantiate and call ``reply``. But for your convention and reusability,
    you can inherit the class to avoid boilerplate code. See 'example_api/bot.py' and '***handler.py'

    When list of renderers passed as ``renderers``, appropriate renderer used according to
    ``env.api``. But when single renderer passed, it is used as renderer.

    Usage::

        >>> from bottoku import Bot, Environment, IncomingMessage
        >>> from bottoku.repository.dict_repository import DictRepository
        >>> from bottoku.api.facebook.renderer import FacebookRenderer
        >>> env = Environment(api='api_name')
        >>> bot = Bot(env,
        >>>           [...],  # actions to reply
        >>>           DictRepository(),  # your favorite repository to store receivers' data
        >>>           FacebookRenderer(env, '...token...'))
        >>> bot.reply(IncomingMessage(message), user_id)

    :param bottoku.Environment env:
    :param list[function] routes:
    :param bottoku.repository.Repository receiver_repository:
    :param bottoku.renderer.Renderer | list[bottoku.renderer.Renderer] renderers: list of renderers, or renderer to use.
    """

    def __init__(self, env, routes, receiver_repository, renderers):
        self.env = env
        self.routes = routes
        self.receiver_repository = receiver_repository

        if isinstance(renderers, list):
            self.renderer = {r.api: r for r in renderers}[env.api]
        else:
            self.renderer = renderers

    def reply(self, message, receiver_id):
        """Handles message and reply.

        In this method, the following operations are executed.

        - calls an action which matches to ``@route`` condition first
        - generates messages to reply by calling an action
        - make requests to API by calling renderer's ``render`` function
        - finally, stores a flag to receiver if a flag is defined via ``@route``

        :param message: incoming message to reply. For convenience, IncomingMessage type is preferred
        :param receiver_id: user's id to reply to
        """
        def render(messages):
            self.renderer.render(messages, receiver_id)

        context = self.receiver_repository.get(receiver_id)
        for route in self.routes:
            match, action, flag = route(message, context)
            if match:
                action(render, message, context)
                if flag is not None:
                    context.set(flag=flag)
                return
        logging.warn('No action matched. Define fallback action.')
