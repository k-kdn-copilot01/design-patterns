"""
Client code demonstrating real-world Builder pattern usage with house construction.
"""

from house_builder import ModernHouseBuilder, TraditionalHouseBuilder, EcoFriendlyHouseBuilder
from house_director import HouseDirector


def demonstrate_builder_pattern():
    """
    Demonstrate the Builder pattern with different house types and construction sequences.
    """
    print("=== Example Demo: Builder Pattern - House Construction ===\n")
    
    director = HouseDirector()
    
    # Modern House - Basic
    print("1. Modern Basic House:")
    modern_builder = ModernHouseBuilder()
    director.builder = modern_builder
    director.build_basic_house()
    house = modern_builder.house
    print(house.get_description())
    print()
    
    # Traditional House - Family
    print("2. Traditional Family House:")
    traditional_builder = TraditionalHouseBuilder()
    director.builder = traditional_builder
    director.build_family_house()
    house = traditional_builder.house
    print(house.get_description())
    print()
    
    # Eco-Friendly House - Luxury
    print("3. Eco-Friendly Luxury House:")
    eco_builder = EcoFriendlyHouseBuilder()
    director.builder = eco_builder
    director.build_luxury_house()
    house = eco_builder.house
    print(house.get_description())
    print()
    
    # Custom House (without Director)
    print("4. Custom Modern House (without Director):")
    print("🔨 Building custom house...")
    custom_builder = ModernHouseBuilder()
    # Client decides which parts to build
    custom_builder.build_foundation()
    custom_builder.build_walls()
    custom_builder.build_roof()
    custom_builder.build_windows()
    custom_builder.build_doors()
    custom_builder.build_pool()  # Skip garage and garden, add pool
    print("✅ Custom house completed!")
    
    house = custom_builder.house
    print(house.get_description())
    print()
    
    # Comparison - Same sequence, different builders
    print("5. Comparison - Same Family House, Different Styles:")
    print("\n--- Modern Family House ---")
    modern_builder2 = ModernHouseBuilder()
    director.builder = modern_builder2
    director.build_family_house()
    modern_house = modern_builder2.house
    print(modern_house.get_description())
    
    print("\n--- Traditional Family House ---")
    traditional_builder2 = TraditionalHouseBuilder()
    director.builder = traditional_builder2
    director.build_family_house()
    traditional_house = traditional_builder2.house
    print(traditional_house.get_description())
    
    print("\n=== Example Demo Complete ===")


if __name__ == "__main__":
    demonstrate_builder_pattern()
