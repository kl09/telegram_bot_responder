import datetime
from telegram_api import TelegramApi
from responses import TextResponses


class TelegramBot:
    def __init__(self, token: str, interval_update: float = 0.1):
        self.token = token
        self.api_url = "https://api.telegram.org/bot%s/" % token

        self.interval_update = interval_update
        self.response_to_bot = False

    def start(self):
        time_worked = 0
        offset = 0

        while True:
            time = datetime.datetime.now().timestamp()
            if not time_worked or time - time_worked >= self.interval_update:
                updates, last_update = TelegramApi().get_updates(token=self.token, offset=offset)

                if offset is not 0:
                    for update in updates:
                        message = update.get("message", None)
                        if message:
                            self._reply_on_message(message)

                if last_update:
                    offset = int(last_update.get("update_id")) + 1 if last_update else offset

                time_worked = time

    def _reply_on_message(self, message: dict):
        response = TelegramBot._get_response_on_text(message.get("text"))
        if response:
            TelegramApi().send_message(
                token=self.token,
                chat_id=message.get('chat').get('id'),
                text=response.get("text"),
                reply_to_message_id=message.get("message_id") if response.get("reply", False) else None,
                parse_mode=response.get("parse_mode") if response.get("parse_mode", None) else None,
            )

    @staticmethod
    def _get_response_on_text(text: str):
        return TextResponses().get_response(text)
