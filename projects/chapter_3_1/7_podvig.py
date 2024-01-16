class SmartPhone:
    def __init__(self, model) -> None:
        self.model = model
        self.apps = []

    def add_app(self, app):
        if not tuple(filter(lambda x: isinstance(x, type(app)), self.apps)):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self, name="ВКонтакте"):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max, name="YouTube"):
        self.name = name
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list, name="Phone"):
        self.name = name
        self.phone_list = phone_list
