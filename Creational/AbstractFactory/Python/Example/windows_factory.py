from gui_factory import Button, Checkbox, GUIFactory

class WindowsButton(Button):
    def paint(self):
        print("Render a button in Windows style")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Render a checkbox in Windows style")

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
