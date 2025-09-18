from abc import ABC, abstractmethod
from meal import Meal


class MealBuilder(ABC):
    """
    Abstract builder interface for creating meals.
    Defines the steps to build different types of meals.
    """
    
    def __init__(self):
        self.meal = Meal()
    
    @abstractmethod
    def build_main_course(self):
        """Build the main course"""
        pass
    
    @abstractmethod
    def build_side_dish(self):
        """Build the side dish"""
        pass
    
    @abstractmethod
    def build_drink(self):
        """Build the drink"""
        pass
    
    @abstractmethod
    def build_dessert(self):
        """Build the dessert"""
        pass
    
    def get_meal(self):
        """Return the built meal"""
        return self.meal
    
    def reset(self):
        """Reset the builder to create a new meal"""
        self.meal = Meal()
        return self
