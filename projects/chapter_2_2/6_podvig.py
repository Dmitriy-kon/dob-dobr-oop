class StackObj:

    def __init__(self, data):
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


class Stack:
    top = None
    __last = None

    def push(self, obj: StackObj):
        if not self.top:
            self.top = obj

        if self.__last:
            self.__last.next = obj

        self.__last = obj

    def pop(self):
        stack_obj = self.top

        if self.__last == self.top:
            result = self.__last
            self.top = None
            self.__last = None
            return result

        while True:
            if stack_obj.next == self.__last:
                result = self.__last
                self.__last = stack_obj
                stack_obj.next = None
                return result
            stack_obj = stack_obj.next

    def get_data(self):
        res = []
        stack_obj = self.top

        while stack_obj:
            res.append(stack_obj.data)
            stack_obj = stack_obj.next

        return res