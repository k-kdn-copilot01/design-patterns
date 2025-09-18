from meal_builder import MealBuilder


class ItalianMealBuilder(MealBuilder):
    """
    Concrete builder for creating Italian-style meals.
    """
    
    def build_main_course(self):
        """Build Italian main course"""
        self.meal.set_main_course("Spaghetti Carbonara", 12.99)
        return self
    
    def build_side_dish(self):
        """Build Italian side dish"""
        self.meal.set_side_dish("Garlic Bread", 4.99)
        return self
    
    def build_drink(self):
        """Build Italian drink"""
        self.meal.set_drink("Chianti Wine", 8.99)
        return self
    
    def build_dessert(self):
        """Build Italian dessert"""
        self.meal.set_dessert("Tiramisu", 6.99)
        return self


class MexicanMealBuilder(MealBuilder):
    """
    Concrete builder for creating Mexican-style meals.
    """
    
    def build_main_course(self):
        """Build Mexican main course"""
        self.meal.set_main_course("Chicken Tacos", 10.99)
        return self
    
    def build_side_dish(self):
        """Build Mexican side dish"""
        self.meal.set_side_dish("Mexican Rice", 3.99)
        return self
    
    def build_drink(self):
        """Build Mexican drink"""
        self.meal.set_drink("Margarita", 7.99)
        return self
    
    def build_dessert(self):
        """Build Mexican dessert"""
        self.meal.set_dessert("Churros", 5.99)
        return self


class AsianMealBuilder(MealBuilder):
    """
    Concrete builder for creating Asian-style meals.
    """
    
    def build_main_course(self):
        """Build Asian main course"""
        self.meal.set_main_course("Chicken Teriyaki", 11.99)
        return self
    
    def build_side_dish(self):
        """Build Asian side dish"""
        self.meal.set_side_dish("Steamed Rice", 2.99)
        return self
    
    def build_drink(self):
        """Build Asian drink"""
        self.meal.set_drink("Green Tea", 2.99)
        return self
    
    def build_dessert(self):
        """Build Asian dessert"""
        self.meal.set_dessert("Mochi Ice Cream", 4.99)
        return self


class HealthyMealBuilder(MealBuilder):
    """
    Concrete builder for creating healthy meals.
    """
    
    def build_main_course(self):
        """Build healthy main course"""
        self.meal.set_main_course("Grilled Salmon", 14.99)
        return self
    
    def build_side_dish(self):
        """Build healthy side dish"""
        self.meal.set_side_dish("Quinoa Salad", 5.99)
        return self
    
    def build_drink(self):
        """Build healthy drink"""
        self.meal.set_drink("Fresh Green Juice", 4.99)
        return self
    
    def build_dessert(self):
        """Build healthy dessert"""
        self.meal.set_dessert("Fruit Bowl", 3.99)
        return self
