from ui_components import Button, Dialog, TextField


class FlatButton(Button):
    """Flat Design Button implementation"""
    
    def render(self) -> str:
        return "Flat Design Button with clean, minimal appearance"
    
    def click(self) -> str:
        return "Flat button clicked with subtle color change"


class FlatDialog(Dialog):
    """Flat Design Dialog implementation"""
    
    def render(self) -> str:
        return "Flat Design Dialog with sharp edges and solid colors"
    
    def show(self) -> str:
        return "Flat dialog shown with fade-in animation"


class FlatTextField(TextField):
    """Flat Design TextField implementation"""
    
    def render(self) -> str:
        return "Flat Design TextField with solid border and clean typography"
    
    def get_text(self) -> str:
        return "Text from Flat TextField"
