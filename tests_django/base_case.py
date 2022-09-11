from chatterbox import ChatBot
from django.test import TransactionTestCase
from tests_django import test_settings


class ChatterBoxTestCase(TransactionTestCase):

    def setUp(self):
        super().setUp()
        self.chatbot = ChatBot(**test_settings.ChatterBox)
