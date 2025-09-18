"""
Application that uses GUI Factory

This represents the client code that works with different GUI factories
to create themed interfaces.
"""

from gui_factory import GUIFactory


class Application:
    """
    Application class that works with any GUI factory.
    The application doesn't know which specific factory it's working with,
    it only knows the abstract interface.
    """
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None
        self.window = None
    
    def create_ui(self) -> None:
        """Create the user interface using the factory"""
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
        self.window = self.factory.create_window()
    
    def render_ui(self) -> None:
        """Render all UI components"""
        if not all([self.button, self.checkbox, self.window]):
            print("Error: UI not created yet. Call create_ui() first.")
            return
        
        print(f"Factory: {self.factory.__class__.__name__}")
        print(f"  Window: {self.window.render()}")
        print(f"  Button: {self.button.render()}")
        print(f"  Checkbox: {self.checkbox.render()}")
    
    def interact_with_ui(self) -> None:
        """Simulate user interactions with the UI"""
        if not all([self.button, self.checkbox, self.window]):
            print("Error: UI not created yet. Call create_ui() first.")
            return
        
        print("\nUser Interactions:")
        print(f"  {self.button.click()}")
        print(f"  {self.checkbox.toggle()}")
        print(f"  Updated checkbox: {self.checkbox.render()}")
        print(f"  {self.window.close()}")


def configure_application(os_type: str) -> Application:
    """
    Configure application based on the operating system.
    This simulates how the Abstract Factory pattern allows
    runtime configuration of product families.
    """
    if os_type == "Windows":
        from windows_factory import WindowsFactory
        factory = WindowsFactory()
    elif os_type == "MacOS":
        from macos_factory import MacOSFactory
        factory = MacOSFactory()
    else:
        raise ValueError(f"Unknown OS type: {os_type}")
    
    return Application(factory)
