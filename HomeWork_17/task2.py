class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []




    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"Author: {self.name}"

class Book:
    total_books = 0
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        if isinstance(author, Author):
            self.author = author
        Book.total_books += 1
        author.books.append(self)

    def __repr__(self):
        return f"Book(Name='{self.name}', Year={self.year}, {self.author})"

    def __str__(self):
        return f"Book: {self.name}, Year: {self.year}, Author: {self.author.name}"

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author: Author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        return new_book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"Library: {self.name}"


author1 = Author("Igor", "Kyiv", 1991)
author2 = Author("Vasa", "Odessa", 1991)


new_library = Library("Central library")

book1 = new_library.new_book("Time", 1900, author1)
book2 = new_library.new_book("The Picture of Dorian Gray", 1890, author1)
print(new_library.group_by_author(author1))
print(new_library.group_by_year(1890))

