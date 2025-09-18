class Meal:
    """
    Represents a complex meal with multiple components.
    This is the product that will be built by the Builder pattern.
    """
    
    def __init__(self):
        self.main_course = None
        self.side_dish = None
        self.drink = None
        self.dessert = None
        self.price = 0.0
    
    def set_main_course(self, main_course, price):
        """Set the main course and its price"""
        self.main_course = main_course
        self.price += price
    
    def set_side_dish(self, side_dish, price):
        """Set the side dish and its price"""
        self.side_dish = side_dish
        self.price += price
    
    def set_drink(self, drink, price):
        """Set the drink and its price"""
        self.drink = drink
        self.price += price
    
    def set_dessert(self, dessert, price):
        """Set the dessert and its price"""
        self.dessert = dessert
        self.price += price
    
    def get_description(self):
        """Get a description of the meal"""
        description = "Meal Components:\n"
        if self.main_course:
            description += f"  Main Course: {self.main_course}\n"
        if self.side_dish:
            description += f"  Side Dish: {self.side_dish}\n"
        if self.drink:
            description += f"  Drink: {self.drink}\n"
        if self.dessert:
            description += f"  Dessert: {self.dessert}\n"
        description += f"  Total Price: ${self.price:.2f}"
        return description
    
    def __str__(self):
        return self.get_description()
