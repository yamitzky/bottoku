==================================================
bottoku - Python Chat/Messenger Bot Microframework
==================================================

bottoku(pronounced as *bot-oku*) is a chat bot *micro* framework for Pythonista.

Feature
=======

bottoku is a microframework, however, you can build chat bots without restriction.

For example,

- Integration with web frameworks e.g. flask, django, etc...
- Serverless bots running on AWS Lambda
- Building messages compatible with Line, Facebook, and Slack
- Messages with attachments e.g. images, videos, etc...
- Conversations with contexts: hi! -> who r u? -> john -> hi john, how about...
- Favorite database backend

Compared to Hubot
=================

- No built-in server. If you want to build non-serverless bots, choose favorite web frameworks.
- No built-in binary. bottoku is just a library, so please do ``pip install`` to integrate.
- Very flexible routing system. Conditions are not defined by regex, but by Python's lambda functions.
- And of course, bottoku is a Python framework.

Usage
=====

First, ``pip`` it.::

    pip install bottoku

Then, define actions and views::

  # views.py
  from bottoku.api.facebook.template import TextMessage
  def greeting():  # view is just a function to return a list of messages
      return [TextMesage(text='hello, i am a bot')]
  
  # actions.py
  from bottoku import route
  @route(lambda message, context: 'hello' in message)  # lambda condition to reply
  def say_hello(render, message, context):
      render(greeting())  # call `render` function
      
Next, define a bot class (application class), it is used to define routes and API clients.::

  # mybot.py
  from bottoku import Bot
  from bottoku.renderer.stdout import StdoutRenderer
  from bottoku.api.facebook.renderer import FacebookRenderer
  class MyBot(Bot):
      def __init__(self, env):
          super(MyBot, self).__init__(
            env,
            [
                actions.say_hello,
                # other actions...
            ],
            BlackholeRepository(),  # repository to set user's data
            [
                StdoutRenderer(),
                FacebookRenderer(),
            ]  # API clients
          )
          
Finally, instantiate the bot and call ``reply`` in handler.::

  # handler.py, lambda handler or web frameworks' webhook handler
  def handler():
      message, receiver_id = extract_from_message()
      bot = MyBot(env)
      bot.reply(message, receiver_id)

Currently, I have not prepared docs yet. But you can see examples.

Example
=======

- `example <https://github.com/yamitzky/bottoku/tree/master/example>`_: most basic example
- `example_api <https://github.com/yamitzky/bottoku/tree/master/example_api>`_: advanced example to use Facebook and Slack APIs

Bugs / Feature requests
=======================

`Github's issue <https://github.com/yamitzky/bottoku/issues>`_ or mention to `@yamitzky <https://twitter.com/yamitzky>`_
