class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year

class Lib:
    def __init__(self) -> None:
        self.book_list: list[Book] = list()

    def __add__(self, book: Book):
        if isinstance(book, Book):
            self.book_list.append(book)
        return self

    def __iadd__(self, book: Book):
        if isinstance(book, Book):
            return self + book

    def __sub__(self, book: Book):
        if isinstance(book, Book):
            self.__del_book(book)
        if isinstance(book, int):
            self.book_list.pop(book)
        return self

    def __isub__(self, book: Book):
        if isinstance(book, (Book, int)):
            return self - book
    
    def __len__(self):
        return len(self.book_list)
    
    def __del_book(self, book: Book):
        temp = self.book_list.copy()
        
        for i in temp:
            spam = book.author == i.author and book.title == i.title and book.year == i.year
            
            if spam:
                self.book_list.remove(i)
                break
    
    
    
    
