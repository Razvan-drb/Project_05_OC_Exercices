class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []
    # Ajouter les méthodes ici

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                return True
        return False

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                return True
        return False

    def available_books(self):
        return self.books


    def borrowed_books(self):
        return self.borrow_books

    def display_books(self, books):
        for book in books:
            print(book)


# Exemple d'utilisation
library = Library()
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
library.add_book(Book("1984", "George Orwell", 1949))

print("Available books:")
library.display_books(library.available_books())  # Affiche: Liste des livres disponibles

library.borrow_book("To Kill a Mockingbird")

print("\nBorrowed books:")
library.display_books(library.borrowed_books())  # Affiche: Liste des livres empruntés

print("\nAvailable books after borrowing:")
library.display_books(library.available_books())
