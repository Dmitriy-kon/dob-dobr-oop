stich = [
    "Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня,",
    "Вы не оставите меня.",
]


def get_lst_worlds(worlds):
    symbols = "–-?!,.;"
    return [
        [word.strip(symbols) for word in string.split() if word not in symbols]
        for string in worlds
    ]


class StringText:
    def __init__(self, lst_worlds) -> None:
        self.lst_worlds = lst_worlds

    def __lt__(self, other):
        return len(self.lst_worlds) < len(other.lst_worlds)

    def __le__(self, other):
        return len(self.lst_worlds) <= len(other.lst_worlds)

    def __repr__(self) -> str:
        return f"{self.lst_worlds}"


lst_text = [StringText(i) for i in get_lst_worlds(stich)]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x.lst_worlds), reverse=True)
lst_text_sorted = [" ".join(j for j in i.lst_worlds) for i in lst_text_sorted]

print(lst_text_sorted)


assert all(
    [[True if i in _ else False for i in "–?!,.;"] for _ in stich]
), "в stich есть знаки которые нужно удалить - (–?!,.;)"
assert len(lst_text) == 7 and all(
    True if isinstance(_, StringText) else False for _ in lst_text
), "ошибка в lst_text"

assert lst_text_sorted == [
    "Я к вам пишу чего же боле",
    "Теперь я знаю в вашей воле",
    "Но вы к моей несчастной доле",
    "Что я могу еще сказать",
    "Хоть каплю жалости храня",
    "Вы не оставите меня",
    "Меня презреньем наказать",
], "неверно отсортирован список lst_text_sorted"

assert (
    lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1]
), "метод > работает неверно"
assert lst_text[1] < lst_text[4], "метод < работает неверно"

assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

print("Правильный ответ.")
