#creating the class 
class Book:
    def __init__(self, title, author, isbn, genre, publication_date, availability=True):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._genre = genre
        self._publication_date = publication_date
        self._availability = availability
    #title
    def get_title(self):
        return self._title
    def set_title(self, title):
        self._title = title
    #author
    def get_author(self):
        return self._author
    def set_title(self, author):
        self._title = author
    # isbn
    def get_isbn(self):
        return self._isbn
    def set_isbn(self, isbn):
        self.isbn = isbn

    #genre
    def get_genre(self):
        return self._genre
    def set_genre(self, genre):
        self.genre = genre

    #publication_date
    def get_publication_date(self):
        return self._publication_date
    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    #availability
    def get_availability(self):
        return self._availability
    def set_availability(self, availability):
        self.availability = availability
    