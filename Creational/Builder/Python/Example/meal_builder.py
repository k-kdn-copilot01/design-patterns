from abc import ABC, abstractmethod
from meal import Meal

class MealBuilder(ABC):
    @abstractmethod
    def add_drink(self): pass

    @abstractmethod
    def add_main_course(self): pass

    @abstractmethod
    def add_dessert(self): pass

    @abstractmethod
    def get_meal(self) -> Meal: pass


class VegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_drink(self):
        self.meal.add_item("Juice")

    def add_main_course(self):
        self.meal.add_item("Veg Burger")

    def add_dessert(self):
        self.meal.add_item("Fruit Salad")

    def get_meal(self) -> Meal:
        return self.meal


class NonVegMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_drink(self):
        self.meal.add_item("Coke")

    def add_main_course(self):
        self.meal.add_item("Chicken Burger")

    def add_dessert(self):
        self.meal.add_item("Ice Cream")

    def get_meal(self) -> Meal:
        return self.meal
