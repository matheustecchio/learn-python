class Book:

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"<Book('{self.name}', {self.book_type}, {self.weight})>"
    
    TYPES = ('hardcover','paperback')

    @classmethod
    def hardcover(cls, name, page_weight) -> object:
        return Book(name, Book.TYPES[0], page_weight+100)
    
    @classmethod
    def paperback(cls, name, page_weight) -> object:
        return Book(name, Book.TYPES[1], page_weight)

book1 = Book.hardcover('Harry Potter', 1200)
print(book1) 

book2 = Book.paperback('Hunger Games', 800)
print(book2)