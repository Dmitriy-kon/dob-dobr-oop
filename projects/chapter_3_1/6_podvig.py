class Museum:
    def __init__(self, name) -> None:
        self.name = name
        self.exhibits = []

    def add_exhibit(self, exhibit):
        self.exhibits.append(exhibit)

    def remove_exhibit(self, exhibit):
        self.exhibits.remove(exhibit)

    def get_info_exhibit(self, indx):
        exp = self.exhibits[indx]
        return f"Описание экспоната: {exp.name}: {exp.descr}"


class Picture:
    def __init__(self, name, author, descr) -> None:
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr
