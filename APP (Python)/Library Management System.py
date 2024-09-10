class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book_title):
        book = Book(book_title)
        self.books.append(book)
        print(f"Book '{book_title}' added to the library.")

    def register_patron(self, patron_name):
        patron = Patron(patron_name)
        self.patrons.append(patron)
        print(f"Patron '{patron_name}' registered.")

    def borrow_book(self, patron_name, book_title):
        patron = self.find_patron(patron_name)
        book = self.find_book(book_title)
        if patron and book and not book.is_borrowed:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"Book '{book_title}' borrowed by '{patron_name}'.")
        else:
            print(f"Cannot borrow book '{book_title}'.")

    def return_book(self, patron_name, book_title):
        patron = self.find_patron(patron_name)
        book = self.find_book(book_title)
        if patron and book and book in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book)
            print(f"Book '{book_title}' returned by '{patron_name}'.")
        else:
            print(f"Cannot return book '{book_title}'.")

    def find_patron(self, patron_name):
        for patron in self.patrons:
            if patron.name == patron_name:
                return patron
        print(f"Patron '{patron_name}' not found.")
        return None

    def find_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book
        print(f"Book '{book_title}' not found.")
        return None

library = Library()
library.register_patron("IU")
library.register_patron("Aryan")
library.add_book("Ikigai")
library.add_book("Rich Dad Poor Dad")
library.add_book("Think and Grow Rich")
library.add_book("Atomic Habits")
library.register_patron("MayPal")
library.borrow_book("IU", "Atomic Habits")
library.return_book("MayPal", "Rich Dad Poor Dad")
library.return_book("IU", "Atomic Habits")


