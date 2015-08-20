class Message(object):
    def __init__(self, message='', author=None):
        self._author = author
        self._message = message

    @property
    def author(self):
        return self._author

    @property
    def message(self):
        return self._message


class MessageReceiver(object):
    def __init__(self):
        self._inbox = []

    def tell(self, message):
        assert isinstance(message, Message)
        self._inbox.append(message)

    @property
    def inbox(self):
        return self._inbox
