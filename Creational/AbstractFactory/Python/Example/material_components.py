from ui_components import Button, Dialog, TextField


class MaterialButton(Button):
    """Material Design Button implementation"""
    
    def render(self) -> str:
        return "Material Design Button with elevation and ripple effect"
    
    def click(self) -> str:
        return "Material button clicked with ripple animation"


class MaterialDialog(Dialog):
    """Material Design Dialog implementation"""
    
    def render(self) -> str:
        return "Material Design Dialog with backdrop and smooth transitions"
    
    def show(self) -> str:
        return "Material dialog shown with slide-up animation"


class MaterialTextField(TextField):
    """Material Design TextField implementation"""
    
    def render(self) -> str:
        return "Material Design TextField with floating label and underline"
    
    def get_text(self) -> str:
        return "Text from Material TextField"
