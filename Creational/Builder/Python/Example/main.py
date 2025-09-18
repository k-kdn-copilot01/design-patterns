"""
Builder Pattern - Real World Example

This demonstrates the Builder pattern using a restaurant meal building scenario:
- Meal: The complex product being built
- MealBuilder: Abstract interface for building meals
- Concrete Builders: Italian, Mexican, Asian, and Healthy meal builders
- MealDirector: Orchestrates the meal building process
- RestaurantClient: Uses the pattern to create various meal configurations

Run this file to see the Builder pattern in a real-world context.
"""

from restaurant_client import RestaurantClient


def main():
    """Main function to run the Builder pattern example demo"""
    print("Builder Pattern - Restaurant Meal Example")
    print("=" * 50)
    print()
    
    client = RestaurantClient()
    client.demonstrate_meal_building()
    print("\n" + "="*50 + "\n")
    client.show_menu_options()


if __name__ == "__main__":
    main()
