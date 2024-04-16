from book import Book
from author import Author
from user import User

class Library:
    def __init__(self):
        self._books = []
        self._authors = []
        self._users = []
#books
    def add_book(self, book):
        self._books.append(book)

    def borrow_book(self, user, book):
        if book.is_available():
            book.set_available(False)
            user.borrow_book(book)
        else:
            print("Sorry, the book is not available for borrowing.")

    def return_book(self, user, book):
        if book in user.get_borrowed_books():
            book.set_available(True)
            user.return_book(book)
        else:
            print("You haven't borrowed this book.")

    def get_books(self):
        return self._books
#user
    def add_user(self, user):
        self._users.append(user)

    def search_user(self, library_id):
        for user in self._users:
            if user.get_library_id() == library_id:
                return user
        return None
    
    def get_users(self):
        return self._users
    
#author
    def add_author(self, author):
        self._authors.append(author)

    def search_author(self, name):
        for author in self._authors:
            if author.get_name() == name:
                return author
        return None
    def get_authors(self):
        return self._authors
