from menu import main_menu, book_menu, user_menu, author_menu
from error_handling import handle_error
from library import Library
from book import Book
from author import Author
from user import User
# Main Menu:
# 1. Book Operations
# 2. User Operations
# 3. Author Operations
# 4. Quit

def main():
    library = Library()
    while True:
        main_menu()
        choice = input("What is your choice: ")
        if choice == '1':
            book_menu(library)
        elif choice == '2':
            user_menu(library)
        elif choice == '3':
            author_menu(library)
        elif choice == '4':
            break 
        else:
            handle_error()


# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books

#adding book function 
def book_menu(library):
    while True:
        print("Book Menu:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        choice = input("Enter your choice: ")
        if choice == '1': 
            add_new_book(library)
        elif choice == '2':
            borrow_book(library)
        elif choice == '3':            
            return_book(library)
        elif choice == '4':
            search_book(library)
        elif choice == '5':
            display_all_books(library)
        else:
            handle_error()

def add_new_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date: ")
    new_book = Book(title, author, isbn, genre, publication_date)
    library.add_book(new_book)
    print("Book added successfully.")
#searching for a book
def search_book(library):
    title = input("Enter title of book: ")
    book = library.search_book(title)
    if book is not None:
        print("Book found:")
        print("Title:", book.get_title())
        print("Author:", book.get_author())
        print("ISBN:", book.get_isbn())
        print("Genre:", book.get_genre())
        print("Publication Date:", book.get_publication_date())
        if book.is_available():
            print("Available")
        else:
            print("Not Available")
    else:
        print("Book not found.")
# borrowing book function    
def borrow_book(library):
    library_id = input("Enter your library ID: ")
    title = input("Enter book title to borrow: ")

    user = library.search_user(library_id)
    if user is None:
        print("User not found.")
        return

    book = library.search_book(title)
    if book is None:
        print("Book not found.")
        return

    if not book.is_available():
        print("Book is not available for borrowing.")
        return

    library.borrow_book(user, book)
    print("Book borrowed successfully.")




#returning book function
def return_book(library):
    library_id = input("Enter your library ID: ")
    title = input("Enter title you would like to return: ")

    user = library.search_user(library_id)
    if user is None:
        print("User not found.")
        return

    book = library.search_book(title)
    if book is None:
        print("Book not found.")
        return

    if book not in user.get_borrowed_books():
        print("You haven't borrowed this book.")
        return

    library.return_book(user, book)
    print("Book was returned")

#display all books function
def display_all_books(library):
    books = library.get_books()
    if books:
        print("All Books:")
        for book in books:
            print("Title:", book.get_title())
            print("Author:", book.get_author())
            print("ISBN:", book.get_isbn())
            print("Genre:", book.get_genre())
            print("Publication Date:", book.get_publication_date())
            if book.is_available():
                print("Available")
            else:
                print("Not Available")
            print()
    else:
        print("No books available.")


# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users
def user_menu(library):
    while True:
        choice = input("Enter your choice (1: Add a new user, 2: View user details, 3: Display all users): ")

        if choice == '1':
            add_new_user(library)
        elif choice == '2':
            view_user_details(library)
        elif choice == '3':
            display_all_users(library)
        else:
            handle_error
# add new user function
def add_new_user(library):
    name = input("Enter username: ")
    library_id = input("Enter library ID: ")
    new_user = User(name, library_id)
    library.add_user(new_user)
    print("User was added")

#add view user function
def view_user_details(library):
    library_id = input("Enter library ID of the user: ")
    user = library.search_user(library_id)
    if user is not None:
        print("User Details:")
        print("Name:", user.get_name())
        print("Library ID:", user.get_library_id())
        borrowed_books = user.get_borrowed_books()
        if borrowed_books:
            print("Borrowed Books:")
            for book in borrowed_books:
                print("- Title:", book.get_title())
                print("  Author:", book.get_author())
        else:
            print("No books borrowed.")
    else:
        print("User not found.")

#display all user function
def display_all_users(library):
    users = library.get_users()
    if users:
        print("All Users:")
        for user in users:
            print("Name:", user.get_name())
            print("Library ID:", user.get_library_id())
            print()
    else:
        print("No users available.")



# Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors
def author_menu(library):
    while True:
        print("Author Menu:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_author(library)
        elif choice == '2':
            view_author_details(library)
        elif choice == '3':
            display_all_authors(library)
        else:
            handle_error()

#add author function
def add_new_author(library):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    new_author = Author(name, biography)
    library.add_author(new_author)
    print("Author added successfully.")

#view author details function
def view_author_details(library):
    name = input("Enter author name: ")
    author = library.search_author(name)
    if author is not None:
        print("Author Details:")
        print("Name:", author.get_name())
        print("Biography:", author.get_biography())
    else:
        print("Author not found.")

#display function
def display_all_authors(library):
    authors = library.get_authors()
    if authors:
        print("All Authors:")
        for author in authors:
            print("Name:", author.get_name())
            print("Biography:", author.get_biography())
            print()
    else:
        print("No authors available.")

if __name__ == "__main__":
    main()
