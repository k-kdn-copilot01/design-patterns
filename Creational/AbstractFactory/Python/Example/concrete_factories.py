from ui_factory import UIFactory
from material_components import MaterialButton, MaterialDialog, MaterialTextField
from flat_components import FlatButton, FlatDialog, FlatTextField


class MaterialUIFactory(UIFactory):
    """
    Concrete Factory for Material Design UI components.
    Creates a family of Material Design components that work together.
    """
    
    def create_button(self):
        return MaterialButton()
    
    def create_dialog(self):
        return MaterialDialog()
    
    def create_text_field(self):
        return MaterialTextField()


class FlatUIFactory(UIFactory):
    """
    Concrete Factory for Flat Design UI components.
    Creates a family of Flat Design components that work together.
    """
    
    def create_button(self):
        return FlatButton()
    
    def create_dialog(self):
        return FlatDialog()
    
    def create_text_field(self):
        return FlatTextField()
