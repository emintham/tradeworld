from message import MessageReceiver


class Entity(object):
    def __init__(self):
        self._receiver = MessageReceiver()

    def __lshift__(self, message):
        self._receiver.tell(message)

    def take_action(self):
        pass
