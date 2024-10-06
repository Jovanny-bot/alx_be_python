class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """Initialize a new book with title, author, and its availability status."""
        self.title = title           # Public attribute
        self.author = author         # Public attribute
        self._is_checked_out = False # Private attribute

    def check_out(self):
        """Check out the book if it's available."""
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True  # Successful checkout

    def return_book(self):
        """Return the book to the library."""
        if not self._is_checked_out:
            return False  # Book was not checked out
        self._is_checked_out = False
        return True  # Successful return

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a collection of books in the library."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store instances of Book

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.check_out():
                return True  # Book successfully checked out
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.return_book():
                return True  # Book successfully returned
        return False  # Book not found or was not checked out

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")


