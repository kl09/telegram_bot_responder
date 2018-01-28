import unittest
from telegram_bot import TelegramBot
from responses import TextResponses


class Tests(unittest.TestCase):
    def test_get_direct_response_on_text(self):
        self.assertEqual({"text": "<b>test</b> yourself", "reply": True, "parse_mode": "HTML"},
                         TextResponses()._get_direct_response("test"))

        self.assertEqual({"text": "Nooooooo", "reply": True},
                         TextResponses()._get_direct_response("yes"))

        self.assertEqual({"text": "not lol", "reply": True},
                         TextResponses()._get_direct_response("lol"))

    def test_get_regular_response_on_text(self):
        self.assertEqual({"regex": r"hello", "text": "hello you too", "reply": True},
                         TextResponses()._get_regular_response("hello"))

    def test_telegram_bot_get_response_on_text(self):
        self.assertEqual({"text": "<b>test</b> yourself", "reply": True, "parse_mode": "HTML"},
                         TelegramBot._get_response_on_text("test"))

        self.assertEqual({"regex": r"hello", "text": "hello you too", "reply": True},
                         TelegramBot._get_response_on_text("hello"))


if __name__ == '__main__':
    unittest.main()
