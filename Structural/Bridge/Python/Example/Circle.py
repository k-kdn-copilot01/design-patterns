"""
Bridge Pattern - Real World Example
Circle shape implementation.
"""

from Shape import Shape


class Circle(Shape):
    """
    Concrete implementation of Shape for circles.
    This is a 'Refined Abstraction' in the Bridge pattern.
    """
    
    def __init__(self, x: float, y: float, radius: float, drawing_api):
        """
        Initialize a circle with position, radius, and drawing API.
        
        Args:
            x (float): X coordinate of circle center
            y (float): Y coordinate of circle center
            radius (float): Circle radius
            drawing_api: The drawing API to use
        """
        super().__init__(drawing_api)
        self._x = x
        self._y = y
        self._radius = radius
    
    def draw(self) -> str:
        """
        Draw the circle using the drawing API.
        
        Returns:
            str: Description of the circle drawing operation
        """
        return f"Circle: {self._drawing_api.draw_circle(self._x, self._y, self._radius)}"
    
    def resize(self, factor: float) -> str:
        """
        Resize the circle by changing its radius.
        
        Args:
            factor (float): Resize factor
            
        Returns:
            str: Description of the resize operation
        """
        old_radius = self._radius
        self._radius *= factor
        return f"Circle: Resized radius from {old_radius} to {self._radius} (factor: {factor})"
    
    def get_info(self) -> str:
        """
        Get information about the circle.
        
        Returns:
            str: Circle information
        """
        return f"Circle at ({self._x}, {self._y}) with radius {self._radius}"
