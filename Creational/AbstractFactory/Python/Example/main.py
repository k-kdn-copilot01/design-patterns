from concrete_factories import MaterialUIFactory, FlatUIFactory
from ui_application import UIApplication


def create_ui_application(factory):
    """
    Create and demonstrate a UI application with the given factory.
    """
    app = UIApplication(factory)
    app.create_ui_components()
    app.render_ui()
    app.interact_with_ui()


if __name__ == "__main__":
    print("=== Abstract Factory Pattern - UI Components Example ===\n")
    
    print("1. Creating UI Application with Material Design Theme:")
    print("-" * 50)
    create_ui_application(MaterialUIFactory())
    
    print("\n2. Creating UI Application with Flat Design Theme:")
    print("-" * 50)
    create_ui_application(FlatUIFactory())
    
    print("\n=== Key Benefits Demonstrated ===")
    print("✓ Same client code works with different UI themes")
    print("✓ Components from the same family are guaranteed to be compatible")
    print("✓ Easy to add new themes by creating new concrete factories")
    print("✓ Client code is decoupled from concrete implementations")
