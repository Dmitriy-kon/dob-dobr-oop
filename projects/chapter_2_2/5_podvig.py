class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = width
        self.__height = height
    
    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, new_width):
        if self.__validate_data(new_width):
            self.__width = new_width
            self.show()
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        if self.__validate_data(new_height):
            self.__height= new_height
            self.show()
    
    @staticmethod
    def __validate_data(data):
        return isinstance(data, int) and 0 < data < 10000