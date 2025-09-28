from abc import ABC, abstractmethod
from typing import Any
from Iterator import Iterator


class IterableCollection(ABC):
    """
    Abstract interface for collections that can be iterated over.
    """
    
    @abstractmethod
    def create_iterator(self) -> Iterator:
        """
        Creates and returns an iterator for this collection.
        
        Returns:
            Iterator: An iterator instance for this collection
        """
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """
        Returns the size of the collection.
        
        Returns:
            int: The number of elements in the collection
        """
        pass
    
    @abstractmethod
    def get_item(self, index: int) -> Any:
        """
        Returns the item at the specified index.
        
        Args:
            index (int): The index of the item to retrieve
            
        Returns:
            Any: The item at the specified index
            
        Raises:
            IndexError: If the index is out of bounds
        """
        pass
