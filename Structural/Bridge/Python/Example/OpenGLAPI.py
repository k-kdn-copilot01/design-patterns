"""
Bridge Pattern - Real World Example
OpenGL implementation of the DrawingAPI.
"""

from DrawingAPI import DrawingAPI


class OpenGLAPI(DrawingAPI):
    """
    Concrete implementation of DrawingAPI using OpenGL.
    This represents one platform-specific implementation.
    """
    
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        """
        Draw a circle using OpenGL rendering.
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            radius (float): Circle radius
            
        Returns:
            str: OpenGL-specific circle drawing description
        """
        return f"OpenGL: Drawing circle at ({x}, {y}) with radius {radius} using GPU acceleration"
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> str:
        """
        Draw a rectangle using OpenGL rendering.
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            width (float): Rectangle width
            height (float): Rectangle height
            
        Returns:
            str: OpenGL-specific rectangle drawing description
        """
        return f"OpenGL: Drawing rectangle at ({x}, {y}) with size {width}x{height} using GPU acceleration"
