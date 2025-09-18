from gui_factory import GUIFactory

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):
        self.button.paint()
        self.checkbox.paint()
