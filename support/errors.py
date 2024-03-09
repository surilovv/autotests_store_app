class TokenNotFound(Exception):
    def __init__(self, message="Token not found"):
        super().__init__(message)


class TokenNotGranted(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        self.message = self._create_message()
        super().__init__(self.message)

    def _create_message(self):
        return f"Token not generated. Reason: {self.status_code}"
