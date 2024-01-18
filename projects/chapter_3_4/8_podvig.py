class Item:
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
    
    def __radd__(self, other):
        return other + self.money


class Budget:
    def __init__(self) -> None:
        self.budget = list()

    def add_item(self, item):
        self.budget.append(item)

    def remove_item(self, indx):
        self.budget.pop(indx)

    def get_items(self):
        return self.budget

