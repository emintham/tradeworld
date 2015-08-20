from unittest import TestCase

from tradeworld import Message, MessageReceiver


class MessageTests(TestCase):
    def test_message_initialization(self):
        m = Message()
        self.assertEqual(m.message, '')
        self.assertIsNone(m.author)

        author = 'David Wong'
        message = 'John dies at the End'
        m = Message(message=message, author=author)
        self.assertEqual(m.message, message)
        self.assertEqual(m.author, author)


class MessageReceiverTests(TestCase):
    def setUp(self):
        self.receiver = MessageReceiver()
        self.sender = MessageReceiver()

    def test_tell(self):
        m = Message('buy more eggs', self.sender)
        self.receiver.tell(m)
        self.assertEqual(self.receiver.inbox, [m])

    def test_messages_in_order_received(self):
        m1 = Message('buy more eggs', self.sender)
        m2 = Message('buy a magazine', self.sender)

        self.receiver.tell(m1)
        self.receiver.tell(m2)

        self.assertEqual(self.receiver.inbox [m1, m2])
