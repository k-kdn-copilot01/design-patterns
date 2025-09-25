"""
Bridge Pattern - Real World Example
DirectX implementation of the DrawingAPI.
"""

from DrawingAPI import DrawingAPI


class DirectXAPI(DrawingAPI):
    """
    Concrete implementation of DrawingAPI using DirectX.
    This represents another platform-specific implementation.
    """
    
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        """
        Draw a circle using DirectX rendering.
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            radius (float): Circle radius
            
        Returns:
            str: DirectX-specific circle drawing description
        """
        return f"DirectX: Drawing circle at ({x}, {y}) with radius {radius} using hardware acceleration"
    
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> str:
        """
        Draw a rectangle using DirectX rendering.
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            width (float): Rectangle width
            height (float): Rectangle height
            
        Returns:
            str: DirectX-specific rectangle drawing description
        """
        return f"DirectX: Drawing rectangle at ({x}, {y}) with size {width}x{height} using hardware acceleration"
