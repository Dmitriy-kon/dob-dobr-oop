from typing import Any


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get("login", "")
        self.password = request.get("password", "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, psw):
        return self.min_length <= len(psw) <= self.max_length


class CharsValidator:
    def __init__(self, chars) -> None:
        self.chars = chars

    def __call__(self, chars, *args: Any, **kwds: Any) -> Any:
        return all(i in self.chars for i in chars)
