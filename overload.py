class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.pages + other.pages)
        return NotImplemented

    def __str__(self):
        return f"Book with {self.pages} pages"

book1 = Book(150)
book2 = Book(200)

total_pages = book1 + book2

print(total_pages)  