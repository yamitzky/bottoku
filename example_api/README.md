## Advanced Working Example

In this example, the following features are used:

- `flag` for conversation
- `repository` to remember name
- `renderer`s to request to Facebook and Slack APIs

This example is implemented to fit to production usages. For further information,
see the last part of this page.

### Usage

First, you must set environment values. I use `direnv` to define them and added
`.envrc` to `.gitignore`(It's safe :).

If you do NOT want to use any APIs(it's ok there is CLI example), edit `config.py` and
delete inside `[ ... ]`(NOT entire file).

```
export BOTTOKU_TEST_FACEBOOK_TOKEN=""
export BOTTOKU_TEST_FACEBOOK_RECEIVER_ID=""
export BOTTOKU_TEST_SLACK_WEBHOOK_URL=""
export BOTTOKU_TEST_SLACK_RECEIVER_ID=""
```

Then execute the following command.

```
# for CLI conversation example
python example_api/shell_handler.py
# for Facebook
python example_api/facebook_handler.py "message"
# for Slack
python example_api/slack_handler.py "message"
```

In CLI example, you can have conversations like:

```
$ python example_api/shell_handler.py
input...
hello
[TextMessage(text="hi! what's your name?")]
input...
daniel
[TextMessage(text='oh, your name is daniel? Great!')]
input...
thanks
[TextMessage(text='hi daniel, try to say "hello"')]
input...
```

Cool, the bot can remember my name! Of course I know that you think it is not
smart. But you can build great chat bots by using the `flag` function used
in `actions.py`.

You cannot test conversation in Facebook and Slack examples, because flags are
stored in Python's `dict`. That is, the bot cannot remember your name.

### AWS Lambda and API Gateway

The handlers of `facebook_handler.py` and `slack_handler.py` are designed to
fit to AWS's serverless stack. Their signatures are well known
`handler(event, context)` format.

However, the `repository` used in the example is just a `DictRepository`,
which is an ephemeral repository. When you want to make bots to remember with
serverless architecture, you should implement non-ephemeral repositories such as
`DynamoRepository` or `RedisRepoisitory`. (Then please make pull requests if you
don't mind)

### Multiple APIs

In this example, I chose Facebook's template class as common intermediate
templates of the bot. But of course Facebook's templates cannot be sent to
Slack.

For these situations, make `FacebookToSlackRenderer` and override `convert`
method so that it can convert from Facebook's ones to Slack's ones.

### Use with Web Framework

Perhaps you want to use `Bottoku` with a Python web framework such as flask,
django, tornado. In this case, of course you have to prepare webhooks that
receive messages from Facebook or Slack, and then integrate with Bottoku.

Good news, it is not difficult and `shell_handler.py` is the example.
`Bot` is just a object, so you can instantiate it, set to variable, and reuse
it.
