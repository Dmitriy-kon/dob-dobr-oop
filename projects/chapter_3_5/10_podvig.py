class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, thing):
        self.things.append(thing)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        spam1, spam2 = self.get_things(), other.get_things()

        if len(spam1) != len(spam2):
            return False

        for i in spam1:
            if i not in spam2:
                return False
            if sum(i == j for j in spam2) < 1:
                return False

        return True


class Thing:
    def __init__(self, name, mass) -> None:
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.mass == other.mass and self.name.lower() == other.name.lower()


b1 = Box()
b2 = Box()

b1.add_thing(Thing("мел", 100))
b1.add_thing(Thing("тряпка", 200))
b1.add_thing(Thing("доска", 2000))

b2.add_thing(Thing("тряпка", 200))
b2.add_thing(Thing("мел", 100))
b2.add_thing(Thing("доска", 2000))

res = b1 == b2  # True
print(res)
