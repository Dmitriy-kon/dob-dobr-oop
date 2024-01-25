class Array:
    def __init__(self, max_length, cell) -> None:
        self.max_length = max_length
        self.cell = cell
        self.__array = [self.cell() for _ in range(max_length)]
    
    def __check_index(self, index):
        if not 0 <= index < self.max_length:
            raise IndexError("неверный индекс")
    
    def __getitem__(self, index):
        self.__check_index(index)
        res = self.__array[index]
        if res.value is None:
            return res.start_value
        return res.value
    
    def __setitem__(self, index, value):
        self.__check_index(index)
        self.__array[index].value = value
    
    def __str__(self) -> str:
        return " ".join([str(i.value) if i.value else str(i.start_value) for i in self.__array])


class Integer:
    def __init__(self, start_value: int = 0) -> None:
        self.start_value = start_value
        self.__value = None

    def __check_type(self, value):
        if not isinstance(value, int):
            raise ValueError("должно быть целое число")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__check_type(value)
        self.__value = value

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[2] = 12.2
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел