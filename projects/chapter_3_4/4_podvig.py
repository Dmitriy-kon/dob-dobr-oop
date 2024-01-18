class NewList:
    def __init__(self, lst=None):
        if lst:
            self.__list = list(lst)
        else:
            self.__list = []

    def get_list(self):
        return self.__list

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            # if type(other) not in (list, NewList):
            raise TypeError("Используются только списки или Newlist")

        if isinstance(other, NewList):
            other = other.get_list()

        return NewList(self.__diff_list(self.data, other))

    def __rsub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError("Используются только списки или Newlist")
        if isinstance(other, NewList):
            other = other.get_list()

        return NewList(self.__diff_list(other, self.data))
    @classmethod
    def __diff_lst(cls, mainlist, otherlist):
        if not len(otherlist):
            return mainlist

        spam = list(otherlist)
        return [x for x in mainlist if not cls.__is_elem(x, spam)]

    @staticmethod
    def __is_elem(el1, el2):
        res = any(map(lambda x: type(el1) == type(x) and el1 == x, el2))
        if res:
            el2.remove(el1)
        return res
