import random
from typing import Any

class RandomPassword:
    
    def __init__(self, psw_chars, min_length, max_length) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        res = "".join(random.choice(self.psw_chars) for _ in range(random.randint(self.min_length, self.max_length + 1)))
        return res

lst_pass = [RandomPassword(psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", max_length = 20, min_length = 5)() for _ in range(3)]
print(lst_pass)