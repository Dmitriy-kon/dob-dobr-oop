class Cell:
    def __init__(self, data=0) -> None:
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data


class TableValues:
    def __init__(self, rows, cols, type_data=int) -> None:
        if not type_data:
            raise ValueError("параметр cell не указан")
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.__table = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    def __check_index(self, row, col):
        if not 0 <= row < self.rows or not 0 <= col < self.cols:
            raise IndexError("неверный индекс")

    def __check_type(self, value):
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, item):
        row, col = item
        self.__check_index(row, col)
        return self.__table[row][col].data
    
    def __setitem__(self, key, value):
        row, col = key
        self.__check_index(row, col)
        self.__check_type(value)
        self.__table[row][col].data = value
    
    def __iter__(self):
        return ((j.data for j in i) for i in self.__table)


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
        
assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"