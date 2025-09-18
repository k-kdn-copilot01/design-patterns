"""
Windows Theme Factory Implementation

Creates GUI components with Windows-style appearance and behavior.
"""

from gui_factory import GUIFactory, Button, Checkbox, Window


# Windows-style Products
class WindowsButton(Button):
    """Windows-style button implementation"""
    
    def render(self) -> str:
        return "Rendering Windows-style button with rectangular borders"
    
    def click(self) -> str:
        return "Windows button clicked with system sound"


class WindowsCheckbox(Checkbox):
    """Windows-style checkbox implementation"""
    
    def __init__(self):
        self.checked = False
    
    def render(self) -> str:
        state = "☑" if self.checked else "☐"
        return f"Rendering Windows-style checkbox: {state} (square design)"
    
    def toggle(self) -> str:
        self.checked = not self.checked
        state = "checked" if self.checked else "unchecked"
        return f"Windows checkbox toggled to {state}"


class WindowsWindow(Window):
    """Windows-style window implementation"""
    
    def render(self) -> str:
        return "Rendering Windows-style window with title bar and minimize/maximize/close buttons"
    
    def close(self) -> str:
        return "Windows window closed with fade animation"


# Windows Factory
class WindowsFactory(GUIFactory):
    """
    Factory that creates Windows-themed GUI components.
    All components will have consistent Windows look and feel.
    """
    
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
    
    def create_window(self) -> Window:
        return WindowsWindow()
