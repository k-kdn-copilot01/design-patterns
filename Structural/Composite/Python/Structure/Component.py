from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.parent = None
    
    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """
        pass
    
    @abstractmethod
    def add(self, component: 'Component') -> None:
        """
        In some cases, it would be beneficial to define the child-management
        operations right in the base Component class. This way, you won't need
        to expose any concrete component classes to the client code, even during
        the object tree assembly. The downside is that these methods will be
        empty for the leaf-level components.
        """
        pass
    
    @abstractmethod
    def remove(self, component: 'Component') -> None:
        """
        Remove a child component from this component.
        """
        pass
    
    @abstractmethod
    def get_children(self) -> List['Component']:
        """
        Get all child components.
        """
        pass
    
    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether
        a component can bear children.
        """
        return False
    
    def get_parent(self) -> 'Component':
        """
        Get the parent component.
        """
        return self.parent
    
    def set_parent(self, parent: 'Component') -> None:
        """
        Set the parent component.
        """
        self.parent = parent
