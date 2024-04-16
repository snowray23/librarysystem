class User:
    def __init__(self, name, library_id):
        self._name = name
        self._library_id = library_id
        self._borrowed_books = []

        #name
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

        #library_id
    def get_library_id(self):
        return self._library_id
    def set_library_id(self, library_id):
        self._library_id = library_id

        #borrowed books
    def get_borrowed_books(self):
        return self._borrowed_books
    def get_borrowed_books(self, borrowed_books):
        self._borrowed_books = borrowed_books
        