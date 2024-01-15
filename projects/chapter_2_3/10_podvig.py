class Telecast:
    def __init__(self, id, name, duration) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        if type(value) == int:
            self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if type(value) == int:
            self.__duration = value


class TVProgram:
    def __init__(self, name) -> None:
        self.name = name
        self.items = []

    def add_telecast(self, item):
        self.items.append(item)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)
                break
