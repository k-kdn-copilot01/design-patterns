"""
Prototype Interface

This module defines the abstract base class for the Prototype pattern.
All concrete prototypes must implement the clone() method.
"""
from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    """
    Abstract base class for prototype objects.
    Defines the interface that all concrete prototypes must implement.
    """
    
    @abstractmethod
    def clone(self):
        """
        Create a copy of the current object.
        
        Returns:
            A new instance that is a copy of the current object.
        """
        pass


class ConcretePrototype(Prototype):
    """
    Concrete implementation of the Prototype pattern.
    Demonstrates both shallow and deep copying capabilities.
    """
    
    def __init__(self, name, data=None):
        """
        Initialize the concrete prototype.
        
        Args:
            name (str): Name of the prototype
            data (dict): Optional data dictionary (for deep copy demonstration)
        """
        self.name = name
        self.data = data or {}
        print(f"ConcretePrototype '{name}' created")
    
    def clone(self, deep=False):
        """
        Create a copy of this prototype.
        
        Args:
            deep (bool): If True, perform deep copy; otherwise shallow copy
            
        Returns:
            ConcretePrototype: A new instance that is a copy of this object
        """
        if deep:
            # Deep copy - creates new objects for nested structures
            cloned = copy.deepcopy(self)
            cloned.name = f"{self.name}_deep_clone"
        else:
            # Shallow copy - shares references to nested objects
            cloned = copy.copy(self)
            cloned.name = f"{self.name}_shallow_clone"
        
        print(f"Cloned '{self.name}' -> '{cloned.name}' ({'deep' if deep else 'shallow'} copy)")
        return cloned
    
    def set_data(self, key, value):
        """Set data in the prototype's data dictionary."""
        self.data[key] = value
    
    def get_data(self, key):
        """Get data from the prototype's data dictionary."""
        return self.data.get(key)
    
    def __str__(self):
        return f"ConcretePrototype(name='{self.name}', data={self.data})"


class Client:
    """
    Client class that uses prototypes to create new objects.
    Demonstrates the Prototype pattern in action.
    """
    
    def __init__(self):
        self.prototypes = {}
    
    def register_prototype(self, key, prototype):
        """
        Register a prototype with a key.
        
        Args:
            key (str): Key to identify the prototype
            prototype (Prototype): The prototype object to register
        """
        self.prototypes[key] = prototype
        print(f"Registered prototype with key: '{key}'")
    
    def create_from_prototype(self, key, deep=False):
        """
        Create a new object from a registered prototype.
        
        Args:
            key (str): Key of the registered prototype
            deep (bool): Whether to perform deep copy
            
        Returns:
            Prototype: A new instance cloned from the prototype
        """
        if key not in self.prototypes:
            raise ValueError(f"No prototype registered with key: '{key}'")
        
        prototype = self.prototypes[key]
        return prototype.clone(deep=deep)
    
    def list_prototypes(self):
        """List all registered prototypes."""
        print("Registered prototypes:")
        for key, prototype in self.prototypes.items():
            print(f"  - {key}: {prototype}")
