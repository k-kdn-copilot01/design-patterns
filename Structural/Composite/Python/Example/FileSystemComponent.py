from abc import ABC, abstractmethod
from typing import List


class FileSystemComponent(ABC):
    """
    Base class for file system components (files and directories).
    """
    
    def __init__(self, name: str):
        self.name = name
        self.parent = None
    
    @abstractmethod
    def get_size(self) -> int:
        """
        Get the size of the component in bytes.
        """
        pass
    
    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """
        Display the component with proper indentation.
        """
        pass
    
    @abstractmethod
    def add(self, component: 'FileSystemComponent') -> None:
        """
        Add a child component.
        """
        pass
    
    @abstractmethod
    def remove(self, component: 'FileSystemComponent') -> None:
        """
        Remove a child component.
        """
        pass
    
    @abstractmethod
    def get_children(self) -> List['FileSystemComponent']:
        """
        Get all child components.
        """
        pass
    
    def is_directory(self) -> bool:
        """
        Check if this component is a directory.
        """
        return False
    
    def get_parent(self) -> 'FileSystemComponent':
        """
        Get the parent component.
        """
        return self.parent
    
    def set_parent(self, parent: 'FileSystemComponent') -> None:
        """
        Set the parent component.
        """
        self.parent = parent
