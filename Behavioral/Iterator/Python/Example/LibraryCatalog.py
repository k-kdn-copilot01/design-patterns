from typing import List, Optional, TYPE_CHECKING
from Book import Book

if TYPE_CHECKING:
    from BookIterator import BookIterator, AvailableBooksIterator, GenreIterator


class LibraryCatalog:
    """
    A library catalog that manages a collection of books and provides iteration capabilities.
    """
    
    def __init__(self):
        """
        Initialize an empty library catalog.
        """
        self._books: List[Book] = []
    
    def add_book(self, book: Book) -> None:
        """
        Adds a book to the catalog.
        
        Args:
            book (Book): The book to add to the catalog
        """
        self._books.append(book)
    
    def remove_book(self, isbn: str) -> bool:
        """
        Removes a book from the catalog by ISBN.
        
        Args:
            isbn (str): The ISBN of the book to remove
            
        Returns:
            bool: True if the book was found and removed, False otherwise
        """
        for i, book in enumerate(self._books):
            if book.isbn == isbn:
                del self._books[i]
                return True
        return False
    
    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Finds a book by its ISBN.
        
        Args:
            isbn (str): The ISBN to search for
            
        Returns:
            Optional[Book]: The book if found, None otherwise
        """
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_books_by_author(self, author: str) -> List[Book]:
        """
        Finds all books by a specific author.
        
        Args:
            author (str): The author to search for
            
        Returns:
            List[Book]: List of books by the author
        """
        return [book for book in self._books if author.lower() in book.author.lower()]
    
    def find_books_by_genre(self, genre: str) -> List[Book]:
        """
        Finds all books in a specific genre.
        
        Args:
            genre (str): The genre to search for
            
        Returns:
            List[Book]: List of books in the genre
        """
        return [book for book in self._books if genre.lower() in book.genre.lower()]
    
    def get_available_books(self) -> List[Book]:
        """
        Returns all available books.
        
        Returns:
            List[Book]: List of available books
        """
        return [book for book in self._books if book.is_available]
    
    def get_borrowed_books(self) -> List[Book]:
        """
        Returns all borrowed books.
        
        Returns:
            List[Book]: List of borrowed books
        """
        return [book for book in self._books if not book.is_available]
    
    def get_total_books(self) -> int:
        """
        Returns the total number of books in the catalog.
        
        Returns:
            int: Total number of books
        """
        return len(self._books)
    
    def get_books(self) -> List[Book]:
        """
        Returns all books in the catalog.
        
        Returns:
            List[Book]: All books in the catalog
        """
        return self._books.copy()
    
    def create_iterator(self) -> 'BookIterator':
        """
        Creates a new iterator for the catalog.
        
        Returns:
            BookIterator: A new iterator instance
        """
        from BookIterator import BookIterator
        return BookIterator(self)
    
    def create_available_books_iterator(self) -> 'AvailableBooksIterator':
        """
        Creates an iterator for available books only.
        
        Returns:
            AvailableBooksIterator: A new iterator for available books
        """
        from BookIterator import AvailableBooksIterator
        return AvailableBooksIterator(self)
    
    def create_genre_iterator(self, genre: str) -> 'GenreIterator':
        """
        Creates an iterator for books of a specific genre.
        
        Args:
            genre (str): The genre to filter by
            
        Returns:
            GenreIterator: A new iterator for the specified genre
        """
        from BookIterator import GenreIterator
        return GenreIterator(self, genre)
