"""
Main - Demonstrates the Facade pattern with a real-world smart home example.
This file shows how the Facade pattern simplifies complex home automation operations.
"""

from SmartHomeFacade import SmartHomeFacade


def demonstrate_without_facade():
    """
    Demonstrate how complex it would be to manage a smart home without a Facade.
    This shows the problem that the Facade pattern solves in real-world scenarios.
    """
    print("=" * 70)
    print("DEMONSTRATION: Managing Smart Home WITHOUT Facade (Complex)")
    print("=" * 70)
    
    # Import all subsystems directly
    from LightingSystem import LightingSystem
    from ClimateSystem import ClimateSystem
    from SecuritySystem import SecuritySystem
    from EntertainmentSystem import EntertainmentSystem
    
    # Create instances manually
    lighting = LightingSystem()
    climate = ClimateSystem()
    security = SecuritySystem()
    entertainment = EntertainmentSystem()
    
    print("Homeowner: I want to set up for movie night...")
    print("(This requires coordinating 4 different systems manually)")
    print("-" * 50)
    
    # Homeowner needs to know about all subsystems and their methods
    # This is complex and error-prone
    lighting.turn_off_all_lights()
    lighting.turn_on_living_room()
    lighting.set_brightness(20)
    
    climate.set_temperature(21)
    climate.start_ventilation()
    
    entertainment.turn_on_tv()
    entertainment.change_channel(1)
    entertainment.set_tv_volume(60)
    entertainment.turn_off_music_system()
    entertainment.turn_off_gaming_system()
    
    print("-" * 50)
    print("Homeowner: That was a lot of work! I had to remember:")
    print("- All the lighting methods and brightness levels")
    print("- Climate control settings and ventilation")
    print("- Entertainment system setup and volume control")
    print("- Which systems to turn on/off")
    print()


def demonstrate_with_facade():
    """
    Demonstrate how the Facade pattern simplifies smart home management.
    This shows the solution that the Facade pattern provides in real-world scenarios.
    """
    print("=" * 70)
    print("DEMONSTRATION: Managing Smart Home WITH Facade (Simplified)")
    print("=" * 70)
    
    # Create Smart Home Facade instance
    smart_home = SmartHomeFacade()
    
    print("Homeowner: I want to set up for movie night...")
    print("(This is now a single, simple command)")
    print("-" * 50)
    
    # Homeowner only needs to know about the Facade
    # This is simple and intuitive
    result = smart_home.movie_night()
    print(f"Result: {result}")
    print()
    
    print("Homeowner: Now I want to leave home...")
    print("-" * 50)
    result = smart_home.leave_home()
    print(f"Result: {result}")
    print()
    
    print("Homeowner: I'm back home...")
    print("-" * 50)
    result = smart_home.arrive_home()
    print(f"Result: {result}")
    print()
    
    print("Homeowner: Let's have a party!")
    print("-" * 50)
    result = smart_home.party_mode()
    print(f"Result: {result}")
    print()
    
    print("Homeowner: Time for bed...")
    print("-" * 50)
    result = smart_home.sleep_mode()
    print(f"Result: {result}")
    print()
    
    print("Homeowner: Let me check the status of everything...")
    print("-" * 50)
    smart_home.get_home_status()
    print()


def demonstrate_individual_system_access():
    """
    Demonstrate how the Facade can still provide access to individual systems.
    This shows that the Facade doesn't hide functionality, just simplifies common operations.
    """
    print("=" * 70)
    print("DEMONSTRATION: Individual System Access Through Facade")
    print("=" * 70)
    
    smart_home = SmartHomeFacade()
    
    print("Homeowner: I want to manually adjust just the lighting...")
    print("-" * 50)
    
    # Access individual systems when needed
    lighting = smart_home.get_lighting_system()
    lighting.turn_on_kitchen()
    lighting.set_brightness(80)
    
    print("Homeowner: And now just the climate...")
    print("-" * 50)
    
    climate = smart_home.get_climate_system()
    climate.set_temperature(23)
    climate.set_humidity(50)
    
    print("Homeowner: Perfect! The Facade gives me both simplicity AND control.")
    print()


def main():
    """
    Main function to demonstrate the Facade pattern with real-world smart home example.
    Shows both the problem (without Facade) and the solution (with Facade).
    """
    print("FACADE PATTERN - SMART HOME AUTOMATION DEMONSTRATION")
    print("=" * 70)
    print("The Facade pattern provides a unified interface to a set of")
    print("interfaces in a subsystem. In this example, we'll see how it")
    print("simplifies complex smart home automation operations.")
    print()
    
    # Show the problem
    demonstrate_without_facade()
    
    # Show the solution
    demonstrate_with_facade()
    
    # Show individual system access
    demonstrate_individual_system_access()
    
    print("=" * 70)
    print("DEMONSTRATION COMPLETED")
    print("=" * 70)
    print()
    print("Key Benefits of Facade Pattern in Smart Home:")
    print("1. 🏠 Simplifies complex multi-system operations")
    print("2. 🎯 Provides themed scenarios (movie night, party mode, etc.)")
    print("3. 🔧 Reduces coupling between homeowner and subsystems")
    print("4. 🚀 Makes home automation accessible to non-technical users")
    print("5. 🛡️  Maintains access to individual systems when needed")
    print("6. 📱 Provides a single interface for complex operations")
    print("7. 🎨 Enables consistent user experience across scenarios")
    print()
    print("Real-world applications:")
    print("- Smart home automation systems")
    print("- Home theater setup")
    print("- Car dashboard systems")
    print("- Computer startup/shutdown sequences")
    print("- Database connection management")
    print("- API gateway services")


if __name__ == "__main__":
    main()
