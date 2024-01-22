from pprint import pprint


data = [
    "Балакирев С.М.; программист; 33",
    "Кузнецов А.В.; разведчик-нелегал; 35",
    "Суворов А.В.; полководец; 42",
    "Иванов И.И.; фигурант всех подобных списков; 26",
    "Балакирев С.М.; преподаватель; 33",
]


class Record:
    pk = 0

    def __init__(self, fio, descr, old) -> None:
        self.fio = fio
        self.descr = descr
        self.old = old
        Record.pk += 1
        self.pk = Record.pk

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)
    
    
    def __repr__(self) -> str:
        # return f"Record({self.fio}, {self.descr}, {self.old}, {hash(self), {self.pk}})"
        return f"Record({hash(self), {self.pk}})"


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        for i in self.dict_db:
            if i.pk == pk:
                return i

db = DataBase("data_base.txt")


for i in data:
    fio, descr, old = i.split("; ")
    obj = Record(fio, descr, int(old))
    db.write(obj)

pprint(db.dict_db)


