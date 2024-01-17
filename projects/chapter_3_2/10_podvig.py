from functools import wraps
from typing import Any


class InputValues:
    def __init__(self, render) -> None:
        self.render = render

    def __call__(self, func) -> Any:
        @wraps(func)
        def wrapper(*args, **kwds):
            lst = func()
            return [self.render()(i) for i in lst.split()]

        return wrapper


class RenderDigit:
    def __call__(self, dig):
        dig: str = dig

        if dig.startswith("-") and dig[1:].isdigit():
            return int(dig)
        if dig.isdigit():
            return int(dig)
        return None

@InputValues(RenderDigit)
def input_dg():
    return input()


res = input_dg()