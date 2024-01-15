class StringValue:
    def __init__(self, min_length=2, max_length=50) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self._validate(value):
            setattr(instance, self.name, value)

    def _validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class PriceValue:
    def __init__(self, max_value=10_000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)
