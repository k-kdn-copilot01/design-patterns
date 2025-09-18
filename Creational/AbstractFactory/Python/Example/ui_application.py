from ui_factory import UIFactory
from ui_components import Button, Dialog, TextField


class UIApplication:
    """
    UI Application that uses the Abstract Factory pattern.
    The application can work with any UI factory without knowing the concrete implementation.
    """
    
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = None
        self.dialog = None
        self.text_field = None
    
    def create_ui_components(self):
        """Create UI components using the factory"""
        self.button = self.factory.create_button()
        self.dialog = self.factory.create_dialog()
        self.text_field = self.factory.create_text_field()
    
    def render_ui(self):
        """Render all UI components"""
        if not all([self.button, self.dialog, self.text_field]):
            print("UI components not created yet. Call create_ui_components() first.")
            return
        
        print("=== UI Application Interface ===")
        print(f"Button: {self.button.render()}")
        print(f"Dialog: {self.dialog.render()}")
        print(f"TextField: {self.text_field.render()}")
        print()
    
    def interact_with_ui(self):
        """Simulate user interaction with UI components"""
        if not all([self.button, self.dialog, self.text_field]):
            print("UI components not created yet. Call create_ui_components() first.")
            return
        
        print("=== User Interactions ===")
        print(f"Button click: {self.button.click()}")
        print(f"Dialog show: {self.dialog.show()}")
        print(f"TextField text: {self.text_field.get_text()}")
        print()
