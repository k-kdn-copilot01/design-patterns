from gui_factory import Button, Checkbox, GUIFactory

class MacButton(Button):
    def paint(self):
        print("Render a button in Mac style")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Render a checkbox in Mac style")

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
