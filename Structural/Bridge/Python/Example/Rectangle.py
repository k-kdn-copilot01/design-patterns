"""
Bridge Pattern - Real World Example
Rectangle shape implementation.
"""

from Shape import Shape


class Rectangle(Shape):
    """
    Concrete implementation of Shape for rectangles.
    This is a 'Refined Abstraction' in the Bridge pattern.
    """
    
    def __init__(self, x: float, y: float, width: float, height: float, drawing_api):
        """
        Initialize a rectangle with position, dimensions, and drawing API.
        
        Args:
            x (float): X coordinate of rectangle top-left corner
            y (float): Y coordinate of rectangle top-left corner
            width (float): Rectangle width
            height (float): Rectangle height
            drawing_api: The drawing API to use
        """
        super().__init__(drawing_api)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
    
    def draw(self) -> str:
        """
        Draw the rectangle using the drawing API.
        
        Returns:
            str: Description of the rectangle drawing operation
        """
        return f"Rectangle: {self._drawing_api.draw_rectangle(self._x, self._y, self._width, self._height)}"
    
    def resize(self, factor: float) -> str:
        """
        Resize the rectangle by scaling its dimensions.
        
        Args:
            factor (float): Resize factor
            
        Returns:
            str: Description of the resize operation
        """
        old_width, old_height = self._width, self._height
        self._width *= factor
        self._height *= factor
        return f"Rectangle: Resized from {old_width}x{old_height} to {self._width}x{self._height} (factor: {factor})"
    
    def get_info(self) -> str:
        """
        Get information about the rectangle.
        
        Returns:
            str: Rectangle information
        """
        return f"Rectangle at ({self._x}, {self._y}) with size {self._width}x{self._height}"
