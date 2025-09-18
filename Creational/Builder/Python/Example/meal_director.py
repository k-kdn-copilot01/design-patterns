from meal_builder import MealBuilder


class MealDirector:
    """
    Director class that orchestrates the meal building process.
    Defines different meal configurations and builds them using the provided builder.
    """
    
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self):
        """Get the current meal builder"""
        return self._builder
    
    @builder.setter
    def builder(self, builder: MealBuilder):
        """Set the meal builder to use"""
        self._builder = builder
    
    def build_complete_meal(self):
        """Build a complete meal with all components"""
        self._builder.reset()
        self._builder.build_main_course()
        self._builder.build_side_dish()
        self._builder.build_drink()
        self._builder.build_dessert()
        return self._builder.get_meal()
    
    def build_light_meal(self):
        """Build a light meal with main course and drink only"""
        self._builder.reset()
        self._builder.build_main_course()
        self._builder.build_drink()
        return self._builder.get_meal()
    
    def build_family_meal(self):
        """Build a family meal with main course, side dish, and drink"""
        self._builder.reset()
        self._builder.build_main_course()
        self._builder.build_side_dish()
        self._builder.build_drink()
        return self._builder.get_meal()
    
    def build_dessert_meal(self):
        """Build a dessert-focused meal"""
        self._builder.reset()
        self._builder.build_main_course()
        self._builder.build_dessert()
        return self._builder.get_meal()
    
    def build_custom_meal(self, components):
        """Build a custom meal with specified components"""
        self._builder.reset()
        if 'main' in components:
            self._builder.build_main_course()
        if 'side' in components:
            self._builder.build_side_dish()
        if 'drink' in components:
            self._builder.build_drink()
        if 'dessert' in components:
            self._builder.build_dessert()
        return self._builder.get_meal()
