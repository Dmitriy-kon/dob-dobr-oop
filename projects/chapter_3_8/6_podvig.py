class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    def __repr__(self) -> str:
        return f"StackObj({self.data},)"


class Stack:
    __top = None

    @property
    def top(self):
        return self.__top

    def push(self, obj: StackObj):
        if not self.__top:
            self.__top = obj
            return

        spam = self._get_last_object()
        spam.next = obj

    def _get_last_object(self):
        obj = self.__top
        while obj:
            if obj.next:
                obj = obj.next
            else:
                return obj

    def pop(self):
        if not self.__top:
            raise AttributeError("Стек пустой")
        obj = self.__top
        last = self._get_last_object()

        while obj:
            if obj.next:
                obj = obj.next

            if obj.next == last:
                spam = obj.next
                obj.next = None
                return spam

    # def __getitem__(self, index):
    #     if index < 0:
    #         raise IndexError
    #     return list(iter(self))[index]
    
    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError(f"{index} больше максимального значения или меньше 0")
        spam = 0
        obj = self.__top
        
        while obj:
            if spam == index:
                return obj
            spam += 1
            obj = obj.next
    
    def __setitem__(self, index, value):
        if not 0 <= index < len(self):
            raise IndexError(f"{index} больше максимального значения или меньше 0")
        spam = 0
        obj = self.__top
        
        while obj:
            if spam == index:
                obj.data = value.data
                return
            spam += 1
            obj = obj.next
        
    
    def __len__(self):
        return len(list(iter(self)))
    
    def __iter__(self):
        obj = self.__top
        while obj:
            yield obj
            obj = obj.next


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
# print(st.top)
# for i in st:
#     print(i, end=" ")
# print()

# print(st.pop())

# for i in st:
#     print(i, end=" ")
# print()
st[2] = StackObj("obj3_SET")

for i in range(len(st)):
    print(st[i].data, end=" ")