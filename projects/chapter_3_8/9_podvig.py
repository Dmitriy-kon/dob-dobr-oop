class Thing:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
    


class Bag:
    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self._bag = []
    
    def add_thing(self, thing: Thing):
        self._check_weight(thing)
        self._bag.append(thing)
    
    def _check_weight(self, thing, old_weight = 0):
        if self._get_weight(old_weight) + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
    
    def _get_weight(self, old_weight):
        return sum(i.weight for i in self._bag) - old_weight

    def _check_index(self, index):
        if not 0 <= index < len(self._bag):
            raise IndexError('неверный индекс')
    
    def __getitem__(self, index):
        self._check_index(index)
        return self._bag[index]

    def __setitem__(self, index, value):
        self._check_index(index)
        old_value = self._bag[index].weight
        self._check_weight(value, old_value)
        self._bag[index] = value
    
    def __delitem__(self, index):
        self._check_index(index)
        del self._bag[index]

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"