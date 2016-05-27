# -*- coding: utf-8 -*-


class Bot(object):
    def __init__(self, env, routes, receiver_repository, renderers):
        self.env = env
        self.routes = routes
        self.receiver_repository = receiver_repository

        if not isinstance(renderers, list):
            self.renderer = renderers
        else:
            self.renderers = {r.api: r for r in renderers}

    def get_renderer(self):
        if hasattr(self, 'renderer'):
            return self.renderer
        else:
            return self.renderers[self.env.api]

    def reply(self, message, receiver_id):
        context = self.receiver_repository.get(receiver_id)
        renderer = self.get_renderer()

        def render(messages):
            renderer.render(messages, receiver_id)

        for route in self.routes:
            match, action, flag = route(message, context)
            if match:
                action(render, message, context)
                if flag is not None:
                    context.set(flag=flag)
                return
