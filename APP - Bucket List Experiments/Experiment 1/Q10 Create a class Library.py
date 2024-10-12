""" Create a class Library with a class variable book_count to keep track of the number of books.
Implement an instance method add_book() that increases the book_count. Create a method to get
the total number of books from the class variable. Demonstrate adding books and retrieving the
count.
Concepts Covered: Static Variables, Class Variables, Instance Methods """

class Library:
    book_count = 0

    def add_book(self):
        Library.book_count += 1  

    def get_total_books(self):
        return Library.book_count

library = Library()

library.add_book()
library.add_book()
library.add_book()

total_books = library.get_total_books()

print("Total number of books in the library:", total_books) 
