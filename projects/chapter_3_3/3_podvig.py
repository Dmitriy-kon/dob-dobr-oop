class Model:
    def __init__(self) -> None:
        self.query_info = {}

    def query(self, *args, **kwargs):
        self.query_info = kwargs

    def __str__(self) -> str:
        if self.query_info:
            res = ", ".join(
                f"{key} = {value}" for key, value in self.query_info.items()
            )
            return f"Model: {res}"
        return "Model"
