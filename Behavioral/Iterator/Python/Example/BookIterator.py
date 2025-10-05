from typing import Optional
from Book import Book
from LibraryCatalog import LibraryCatalog


class BookIterator:
    """
    Iterator for iterating through all books in a library catalog.
    """
    
    def __init__(self, catalog: LibraryCatalog):
        """
        Initialize the iterator with a library catalog.
        
        Args:
            catalog (LibraryCatalog): The catalog to iterate over
        """
        self._catalog = catalog
        self._current_index = 0
    
    def has_next(self) -> bool:
        """
        Returns True if there are more books to iterate over.
        
        Returns:
            bool: True if there are more books
        """
        return self._current_index < self._catalog.get_total_books()
    
    def next(self) -> Book:
        """
        Returns the next book in the iteration.
        
        Returns:
            Book: The next book in the catalog
            
        Raises:
            StopIteration: If there are no more books to iterate
        """
        if not self.has_next():
            raise StopIteration("No more books to iterate")
        
        books = self._catalog.get_books()
        book = books[self._current_index]
        self._current_index += 1
        return book
    
    def reset(self) -> None:
        """
        Resets the iterator to the beginning of the catalog.
        """
        self._current_index = 0
    
    def get_current_index(self) -> int:
        """
        Returns the current index position.
        
        Returns:
            int: The current index
        """
        return self._current_index


class AvailableBooksIterator:
    """
    Iterator for iterating through only available books in a library catalog.
    """
    
    def __init__(self, catalog: LibraryCatalog):
        """
        Initialize the iterator with a library catalog.
        
        Args:
            catalog (LibraryCatalog): The catalog to iterate over
        """
        self._catalog = catalog
        self._available_books = catalog.get_available_books()
        self._current_index = 0
    
    def has_next(self) -> bool:
        """
        Returns True if there are more available books to iterate over.
        
        Returns:
            bool: True if there are more available books
        """
        return self._current_index < len(self._available_books)
    
    def next(self) -> Book:
        """
        Returns the next available book in the iteration.
        
        Returns:
            Book: The next available book
            
        Raises:
            StopIteration: If there are no more available books to iterate
        """
        if not self.has_next():
            raise StopIteration("No more available books to iterate")
        
        book = self._available_books[self._current_index]
        self._current_index += 1
        return book
    
    def reset(self) -> None:
        """
        Resets the iterator to the beginning of the available books.
        """
        self._current_index = 0
        # Refresh the available books list in case books were borrowed/returned
        self._available_books = self._catalog.get_available_books()
    
    def get_current_index(self) -> int:
        """
        Returns the current index position.
        
        Returns:
            int: The current index
        """
        return self._current_index


class GenreIterator:
    """
    Iterator for iterating through books of a specific genre in a library catalog.
    """
    
    def __init__(self, catalog: LibraryCatalog, genre: str):
        """
        Initialize the iterator with a library catalog and genre filter.
        
        Args:
            catalog (LibraryCatalog): The catalog to iterate over
            genre (str): The genre to filter by
        """
        self._catalog = catalog
        self._genre = genre
        self._genre_books = catalog.find_books_by_genre(genre)
        self._current_index = 0
    
    def has_next(self) -> bool:
        """
        Returns True if there are more books of the specified genre to iterate over.
        
        Returns:
            bool: True if there are more books of the genre
        """
        return self._current_index < len(self._genre_books)
    
    def next(self) -> Book:
        """
        Returns the next book of the specified genre in the iteration.
        
        Returns:
            Book: The next book of the genre
            
        Raises:
            StopIteration: If there are no more books of the genre to iterate
        """
        if not self.has_next():
            raise StopIteration(f"No more {self._genre} books to iterate")
        
        book = self._genre_books[self._current_index]
        self._current_index += 1
        return book
    
    def reset(self) -> None:
        """
        Resets the iterator to the beginning of the genre books.
        """
        self._current_index = 0
        # Refresh the genre books list in case books were added/removed
        self._genre_books = self._catalog.find_books_by_genre(self._genre)
    
    def get_current_index(self) -> int:
        """
        Returns the current index position.
        
        Returns:
            int: The current index
        """
        return self._current_index
    
    def get_genre(self) -> str:
        """
        Returns the genre this iterator is filtering by.
        
        Returns:
            str: The genre filter
        """
        return self._genre
