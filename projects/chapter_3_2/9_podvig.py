class InputDigits:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.func().split()]


@InputDigits
def input_dig():
    return input()

res = input_dig()
