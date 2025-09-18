"""
MacOS Theme Factory Implementation

Creates GUI components with MacOS-style appearance and behavior.
"""

from gui_factory import GUIFactory, Button, Checkbox, Window


# MacOS-style Products
class MacOSButton(Button):
    """MacOS-style button implementation"""
    
    def render(self) -> str:
        return "Rendering MacOS-style button with rounded corners and gradient"
    
    def click(self) -> str:
        return "MacOS button clicked with elegant haptic feedback"


class MacOSCheckbox(Checkbox):
    """MacOS-style checkbox implementation"""
    
    def __init__(self):
        self.checked = False
    
    def render(self) -> str:
        state = "✓" if self.checked else "○"
        return f"Rendering MacOS-style checkbox: {state} (circular design)"
    
    def toggle(self) -> str:
        self.checked = not self.checked
        state = "checked" if self.checked else "unchecked"
        return f"MacOS checkbox smoothly animated to {state}"


class MacOSWindow(Window):
    """MacOS-style window implementation"""
    
    def render(self) -> str:
        return "Rendering MacOS-style window with traffic light buttons (red, yellow, green)"
    
    def close(self) -> str:
        return "MacOS window closed with smooth scaling animation"


# MacOS Factory
class MacOSFactory(GUIFactory):
    """
    Factory that creates MacOS-themed GUI components.
    All components will have consistent MacOS look and feel.
    """
    
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()
    
    def create_window(self) -> Window:
        return MacOSWindow()
