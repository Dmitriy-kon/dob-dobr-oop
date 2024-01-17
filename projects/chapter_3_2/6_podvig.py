from typing import Any


class RenderList:
    def __init__(self, type_list) -> None:
        self.type_list = type_list
        self._validate()

    def _validate(self):
        if self.type_list not in ["ul", "ol"]:
            self.type_list = "ul"
    
    def _render(self, lst):
        body = "\n".join(f"<li>{i}</li>" for i in lst)
        return f"<{self.type_list}>\n{body}</{self.type_list}>"

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self._render(args[0])


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)
