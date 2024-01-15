class Car:
    __model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if isinstance(new_model, str) and 2 <= len(new_model) <= 100:
            self.__model = new_model


car = Car()
car.model = "Toyota"
