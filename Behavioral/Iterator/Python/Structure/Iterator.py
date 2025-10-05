from abc import ABC, abstractmethod
from typing import Any


class Iterator(ABC):
    """
    Abstract Iterator interface that defines the contract for iterating over collections.
    """
    
    @abstractmethod
    def has_next(self) -> bool:
        """
        Returns True if the iteration has more elements.
        
        Returns:
            bool: True if there are more elements to iterate over
        """
        pass
    
    @abstractmethod
    def next(self) -> Any:
        """
        Returns the next element in the iteration.
        
        Returns:
            Any: The next element in the collection
            
        Raises:
            StopIteration: If there are no more elements to iterate
        """
        pass
    
    @abstractmethod
    def reset(self) -> None:
        """
        Resets the iterator to the beginning of the collection.
        """
        pass
