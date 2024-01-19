class Money:
    def __init__(self, money=0) -> None:
        self.__volume = money
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    def convert(self, currency):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        return round(self.volume / self.cb.rates[currency], 1)

    def __lt__(self, other):
        return self.convert(self._type) < other.convert(other._type)

    def __le__(self, other):
        return self.convert(self._type) <= other.convert(other._type)

    def __eq__(self, other):
        return self.convert(self._type) == other.convert(other._type)


class CentralBank:
    rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money: Money):
        money.cb = cls


class MoneyR(Money):
    _type = "rub"


class MoneyD(Money):
    _type = "dollar"


class MoneyE(Money):
    _type = "euro"


CentralBank.rates = {"rub": 72.5, "dollar": 1.0, "euro": 1.15}

r = MoneyR(45000)
d = MoneyD(500)

# CentralBank.register(r)
CentralBank.register(d)

print(r.convert("rub"))
print(d.convert("dollar"))

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
