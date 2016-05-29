## Minimum Working Example

This is an example of a minimum implementation. If you want to know how to use
"Bottoku" for real APIs, e.g. Facebook or Slack, see 'example_api' directory.

The bot receives messages from arguments via CLI, and then it calculates, tell a
meaning of "42", or echoes messages three times. These are `action` s.

It does not use any API, but implements actions(=routing and reply logic), a
customized `Bot` class(i.e. application class), and a handler to receive
 messages.

### Usage

```
python example/handler.py "Your message"
```

Say,

```
$ python example/handler.py "Hello"
# "hellohellohello"

$ python example/handler.py "(42 + 3) * 10 ** 2"
# "4500"

$ python example/handler.py "42"
# the Answer to the Ultimate Question of Life, the Universe, and Everything
```
