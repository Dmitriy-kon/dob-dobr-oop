from typing import Any


class DigitRetrieve:
    def __call__(self, dig, *args: Any, **kwds: Any) -> Any:
        try:
            return int(dig)
        except ValueError:
            return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)