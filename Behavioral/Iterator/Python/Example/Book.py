from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    """
    Represents a book in the library system.
    """
    isbn: str
    title: str
    author: str
    genre: str
    year_published: int
    is_available: bool = True
    
    def __str__(self) -> str:
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} ({self.year_published}) - {status}"
    
    def borrow(self) -> bool:
        """
        Attempts to borrow the book.
        
        Returns:
            bool: True if the book was successfully borrowed, False if already borrowed
        """
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self) -> bool:
        """
        Returns the book to the library.
        
        Returns:
            bool: True if the book was successfully returned, False if already available
        """
        if not self.is_available:
            self.is_available = True
            return True
        return False
