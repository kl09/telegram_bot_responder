import re


class TextResponses:
    DIRECT = {
        "test": {"text": "<b>test</b> yourself", "reply": True, "parse_mode": "HTML"},
        "yes": {"text": "Nooooooo", "reply": True},
        "lol": {"text": "not lol", "reply": True},
    }

    REGULAR = [
        {"regex": r"hello", "text": "hello you too", "reply": True},
    ]

    def get_response(self, text: str):
        direct_response = self._get_direct_response(text)

        if direct_response:
            return direct_response
        else:
            return self._get_regular_response(text)

    def _get_direct_response(self, text: str):
        return self.DIRECT.get(text)

    def _get_regular_response(self, text: str):
        for response in self.REGULAR:
            result = re.match(response.get("regex"), text, re.IGNORECASE)
            if result:
                return response

        return None
