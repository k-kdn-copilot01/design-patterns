from typing import Any
from Iterator import Iterator
from IterableCollection import IterableCollection


class ConcreteIterator(Iterator):
    """
    Concrete implementation of Iterator for iterating over a collection.
    """
    
    def __init__(self, collection: IterableCollection):
        """
        Initialize the iterator with a collection.
        
        Args:
            collection (IterableCollection): The collection to iterate over
        """
        self._collection = collection
        self._current_index = 0
    
    def has_next(self) -> bool:
        """
        Returns True if there are more elements to iterate over.
        
        Returns:
            bool: True if current index is less than collection size
        """
        return self._current_index < self._collection.get_size()
    
    def next(self) -> Any:
        """
        Returns the next element in the iteration and advances the index.
        
        Returns:
            Any: The next element in the collection
            
        Raises:
            StopIteration: If there are no more elements to iterate
        """
        if not self.has_next():
            raise StopIteration("No more elements to iterate")
        
        item = self._collection.get_item(self._current_index)
        self._current_index += 1
        return item
    
    def reset(self) -> None:
        """
        Resets the iterator to the beginning of the collection.
        """
        self._current_index = 0
    
    def get_current_index(self) -> int:
        """
        Returns the current index position of the iterator.
        
        Returns:
            int: The current index
        """
        return self._current_index
