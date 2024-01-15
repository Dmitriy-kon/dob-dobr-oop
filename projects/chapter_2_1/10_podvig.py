import random


class EmailValidator:
    __dop_syb = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@._"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return ''.join(random.choice(cls.__dop_syb) for i in range(20)) + '@gmail.com'
        pass

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email) and cls.valid_char(email) and "@" in email:
            index = email.find("@")
            start, end = email[:index], email[index + 1:]
            return len(start) <= 100 and len(end) <= 50 and cls.valid_dot(end) and end.count(
                ".") >= 1 and cls.valid_dot(start)
        return False

    @classmethod
    def valid_char(cls, email):
        return all(map(lambda x: x in cls.__dop_syb, email))

    @staticmethod
    def valid_dot(text):
        dot = text[text.find(".") + 1]
        return dot != '.'

    @staticmethod
    def __is_email_str(email):
        return type(email) == str