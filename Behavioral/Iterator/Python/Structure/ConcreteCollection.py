from typing import Any, List
from IterableCollection import IterableCollection
from ConcreteIterator import ConcreteIterator


class ConcreteCollection(IterableCollection):
    """
    Concrete implementation of a collection that can be iterated over.
    """
    
    def __init__(self):
        """
        Initialize an empty collection.
        """
        self._items: List[Any] = []
    
    def add_item(self, item: Any) -> None:
        """
        Adds an item to the collection.
        
        Args:
            item (Any): The item to add to the collection
        """
        self._items.append(item)
    
    def remove_item(self, item: Any) -> bool:
        """
        Removes an item from the collection.
        
        Args:
            item (Any): The item to remove from the collection
            
        Returns:
            bool: True if the item was found and removed, False otherwise
        """
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False
    
    def create_iterator(self) -> ConcreteIterator:
        """
        Creates and returns a new iterator for this collection.
        
        Returns:
            ConcreteIterator: A new iterator instance
        """
        return ConcreteIterator(self)
    
    def get_size(self) -> int:
        """
        Returns the number of items in the collection.
        
        Returns:
            int: The size of the collection
        """
        return len(self._items)
    
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
        if 0 <= index < len(self._items):
            return self._items[index]
        else:
            raise IndexError(f"Index {index} is out of bounds for collection of size {len(self._items)}")
    
    def is_empty(self) -> bool:
        """
        Returns True if the collection is empty.
        
        Returns:
            bool: True if the collection has no items
        """
        return len(self._items) == 0
    
    def clear(self) -> None:
        """
        Removes all items from the collection.
        """
        self._items.clear()
