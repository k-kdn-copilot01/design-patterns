"""
Real-world Abstract Factory Example - GUI Themes

This example demonstrates the Abstract Factory pattern using a GUI application
that can be configured to use different themes (Windows or MacOS style).
"""

from application import Application, configure_application
from windows_factory import WindowsFactory
from macos_factory import MacOSFactory


def demo_direct_factory_usage():
    """Demo using factories directly"""
    print("=== Direct Factory Usage Demo ===\n")
    
    # Demo 1: Windows Theme
    print("1. Creating Windows-themed application:")
    windows_app = Application(WindowsFactory())
    windows_app.create_ui()
    windows_app.render_ui()
    windows_app.interact_with_ui()
    print()
    
    # Demo 2: MacOS Theme
    print("2. Creating MacOS-themed application:")
    macos_app = Application(MacOSFactory())
    macos_app.create_ui()
    macos_app.render_ui()
    macos_app.interact_with_ui()
    print()


def demo_runtime_configuration():
    """Demo runtime configuration based on OS detection"""
    print("=== Runtime Configuration Demo ===\n")
    
    # Simulate different OS environments
    operating_systems = ["Windows", "MacOS"]
    
    for os_type in operating_systems:
        print(f"Detected OS: {os_type}")
        app = configure_application(os_type)
        app.create_ui()
        app.render_ui()
        app.interact_with_ui()
        print()


def demo_compatibility():
    """Demo showing product compatibility within families"""
    print("=== Product Family Compatibility Demo ===\n")
    
    print("Mixing products from different families would break compatibility!")
    print("Abstract Factory ensures products from the same family work together.\n")
    
    # Show consistent theming
    print("Windows family - all components have consistent styling:")
    windows_factory = WindowsFactory()
    win_button = windows_factory.create_button()
    win_checkbox = windows_factory.create_checkbox()
    win_window = windows_factory.create_window()
    
    print(f"  {win_button.render()}")
    print(f"  {win_checkbox.render()}")
    print(f"  {win_window.render()}")
    print()
    
    print("MacOS family - all components have consistent styling:")
    macos_factory = MacOSFactory()
    mac_button = macos_factory.create_button()
    mac_checkbox = macos_factory.create_checkbox()
    mac_window = macos_factory.create_window()
    
    print(f"  {mac_button.render()}")
    print(f"  {mac_checkbox.render()}")
    print(f"  {mac_window.render()}")


def main():
    """Main function demonstrating Abstract Factory pattern with GUI themes"""
    print("=== Abstract Factory Pattern - GUI Themes Example ===\n")
    
    demo_direct_factory_usage()
    demo_runtime_configuration()
    demo_compatibility()
    
    print("\n=== Example Demo Complete ===")


if __name__ == "__main__":
    main()
