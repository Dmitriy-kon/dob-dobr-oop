class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    def __gt__(self, other):
        return (self.a * self.b * self.c) > (other.a * other.b * other.c)

    def __ge__(self, other):
        return (self.a * self.b * self.c) >= (other.a * other.b * other.c)

    def __repr__(self) -> str:
        return f"{self.a}, {self.b}, {self.c} and dimensions {self.a * self.b * self.c}"

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__validate(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__validate(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__validate(value):
            self.__c = value

    @classmethod
    def __validate(cls, data: int):
        return cls.MIN_DIMENSION <= data <= cls.MAX_DIMENSION


class ShopItem:
    def __init__(self, name: str, price: int | float, dim: Dimensions) -> None:
        self.name = name
        self.price = price
        self.dim = dim

    def __repr__(self) -> str:
        return f"{self.name}, {self.price}, {self.dim}"


lst_shop = [
    ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
    ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
    ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
    ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)),
]

lst_shop_sorted = sorted(
    lst_shop, key=lambda item: item.dim.a * item.dim.b * item.dim.c
)

for i in lst_shop:
    print(i)
print()
for i in lst_shop_sorted:
    print(i)
