"""
Prototype Pattern - Structure Implementation
Core classes demonstrating the Prototype pattern structure
"""

from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    """
    Abstract Prototype class that declares clone interface
    """
    
    @abstractmethod
    def clone(self):
        """
        Abstract method for cloning the object
        """
        pass
    
    @abstractmethod
    def get_info(self):
        """
        Abstract method to get object information
        """
        pass


class ConcretePrototypeA(Prototype):
    """
    Concrete Prototype A - implements clone method
    """
    
    def __init__(self, value: str, data: list = None):
        self.value = value
        self.data = data or []
        self.id = id(self)
    
    def clone(self):
        """
        Shallow clone implementation
        """
        return copy.copy(self)
    
    def deep_clone(self):
        """
        Deep clone implementation
        """
        return copy.deepcopy(self)
    
    def get_info(self):
        return f"ConcretePrototypeA(id={self.id}, value='{self.value}', data={self.data})"
    
    def add_data(self, item):
        self.data.append(item)


class ConcretePrototypeB(Prototype):
    """
    Concrete Prototype B - implements clone method with different behavior
    """
    
    def __init__(self, name: str, config: dict = None):
        self.name = name
        self.config = config or {}
        self.id = id(self)
    
    def clone(self):
        """
        Shallow clone implementation
        """
        return copy.copy(self)
    
    def deep_clone(self):
        """
        Deep clone implementation
        """
        return copy.deepcopy(self)
    
    def get_info(self):
        return f"ConcretePrototypeB(id={self.id}, name='{self.name}', config={self.config})"
    
    def update_config(self, key, value):
        self.config[key] = value


class Client:
    """
    Client class that uses prototypes to create new objects
    """
    
    def __init__(self):
        self.prototypes = {}
    
    def register_prototype(self, name: str, prototype: Prototype):
        """
        Register a prototype with a name
        """
        self.prototypes[name] = prototype
    
    def create_object(self, name: str):
        """
        Create a new object by cloning the registered prototype
        """
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            raise ValueError(f"Prototype '{name}' not found")
    
    def create_deep_object(self, name: str):
        """
        Create a new object by deep cloning the registered prototype
        """
        if name in self.prototypes:
            return self.prototypes[name].deep_clone()
        else:
            raise ValueError(f"Prototype '{name}' not found")
