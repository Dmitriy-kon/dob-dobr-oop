class PhoneBook:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, indx):
        self.phones.pop(indx)

    def get_phone_list(self):
        return self.phones


class PhoneNumber:
    def __init__(self, number, fio) -> None:
        self.__number = number
        self.fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, int) and len(str(number)) == 11:
            self.__number = number
        else:
            raise ValueError("Не корректный номер телефона")
