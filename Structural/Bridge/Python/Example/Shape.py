"""
Bridge Pattern - Real World Example
Shape abstraction that uses the DrawingAPI.
"""

from DrawingAPI import DrawingAPI


class Shape:
    """
    The Shape class represents the 'Abstraction' in the Bridge pattern.
    It defines the interface for shapes and maintains a reference to a DrawingAPI.
    """
    
    def __init__(self, drawing_api: DrawingAPI):
        """
        Initialize the shape with a drawing API.
        
        Args:
            drawing_api (DrawingAPI): The concrete drawing API to use
        """
        self._drawing_api = drawing_api
    
    def draw(self) -> str:
        """
        Draw the shape using the provided drawing API.
        This method should be overridden by concrete shapes.
        
        Returns:
            str: Description of the drawing operation
        """
        return "Drawing shape..."
    
    def resize(self, factor: float) -> str:
        """
        Resize the shape by the given factor.
        This method should be overridden by concrete shapes.
        
        Args:
            factor (float): Resize factor
            
        Returns:
            str: Description of the resize operation
        """
        return f"Resizing shape by factor {factor}..."
