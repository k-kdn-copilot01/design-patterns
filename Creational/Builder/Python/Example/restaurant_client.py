from meal_director import MealDirector
from concrete_meal_builders import (
    ItalianMealBuilder, 
    MexicanMealBuilder, 
    AsianMealBuilder, 
    HealthyMealBuilder
)


class RestaurantClient:
    """
    Client class that demonstrates the Builder pattern in a restaurant context.
    Shows how different meal builders can create various meal configurations.
    """
    
    def __init__(self):
        self.director = MealDirector()
    
    def demonstrate_meal_building(self):
        """Demonstrate different meal building scenarios"""
        print("=== Restaurant Meal Builder Demo ===\n")
        
        # Italian meals
        print("1. Italian Cuisine:")
        italian_builder = ItalianMealBuilder()
        self.director.builder = italian_builder
        
        print("   Complete Italian Meal:")
        complete_italian = self.director.build_complete_meal()
        print(f"   {complete_italian}\n")
        
        print("   Light Italian Meal:")
        light_italian = self.director.build_light_meal()
        print(f"   {light_italian}\n")
        
        # Mexican meals
        print("2. Mexican Cuisine:")
        mexican_builder = MexicanMealBuilder()
        self.director.builder = mexican_builder
        
        print("   Family Mexican Meal:")
        family_mexican = self.director.build_family_meal()
        print(f"   {family_mexican}\n")
        
        print("   Dessert Mexican Meal:")
        dessert_mexican = self.director.build_dessert_meal()
        print(f"   {dessert_mexican}\n")
        
        # Asian meals
        print("3. Asian Cuisine:")
        asian_builder = AsianMealBuilder()
        self.director.builder = asian_builder
        
        print("   Complete Asian Meal:")
        complete_asian = self.director.build_complete_meal()
        print(f"   {complete_asian}\n")
        
        # Healthy meals
        print("4. Healthy Cuisine:")
        healthy_builder = HealthyMealBuilder()
        self.director.builder = healthy_builder
        
        print("   Complete Healthy Meal:")
        complete_healthy = self.director.build_complete_meal()
        print(f"   {complete_healthy}\n")
        
        # Custom meals
        print("5. Custom Meal Configurations:")
        print("   Custom Italian meal (main + side + dessert):")
        self.director.builder = ItalianMealBuilder()
        custom_italian = self.director.build_custom_meal(['main', 'side', 'dessert'])
        print(f"   {custom_italian}\n")
        
        print("   Custom Mexican meal (main + drink):")
        self.director.builder = MexicanMealBuilder()
        custom_mexican = self.director.build_custom_meal(['main', 'drink'])
        print(f"   {custom_mexican}\n")
        
        # Direct builder usage (without Director)
        print("6. Direct Builder Usage (without Director):")
        print("   Building Asian meal step by step:")
        asian_builder = AsianMealBuilder()
        asian_meal = (asian_builder
                     .build_main_course()
                     .build_side_dish()
                     .build_drink()
                     .get_meal())
        print(f"   {asian_meal}\n")
        
        print("=== Demo Complete ===")
    
    def show_menu_options(self):
        """Show available menu options for each cuisine"""
        print("=== Available Menu Options ===\n")
        
        cuisines = {
            "Italian": ItalianMealBuilder(),
            "Mexican": MexicanMealBuilder(),
            "Asian": AsianMealBuilder(),
            "Healthy": HealthyMealBuilder()
        }
        
        for cuisine_name, builder in cuisines.items():
            print(f"{cuisine_name} Cuisine:")
            # Build a complete meal to show all options
            builder.build_main_course()
            builder.build_side_dish()
            builder.build_drink()
            builder.build_dessert()
            meal = builder.get_meal()
            print(f"  {meal}\n")


if __name__ == "__main__":
    client = RestaurantClient()
    client.demonstrate_meal_building()
    print("\n" + "="*50 + "\n")
    client.show_menu_options()
