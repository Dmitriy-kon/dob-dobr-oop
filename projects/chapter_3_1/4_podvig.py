from typing import Any

class Product:
    ids = (i for i in range(1, 100))

    def __init__(self, name, weight, price) -> None:
        self.id = next(Product.ids)
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "name" and isinstance(__value, str):
            super().__setattr__(__name, __value)
        elif (
            __name in ("weight", "price", "id")
            and isinstance(__value, (int, float))
            and __value > 0
        ):
            super().__setattr__(__name, __value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, __name: str) -> None:
        if __name == "id":
            raise AttributeError("Атрибут id удалять запрещено.")

        super().__delattr__(__name)


class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)
