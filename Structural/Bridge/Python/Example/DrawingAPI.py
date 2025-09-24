"""
Bridge Pattern - Real World Example
Drawing API interface for different rendering platforms.
"""

from abc import ABC, abstractmethod


class DrawingAPI(ABC):
    """
    The DrawingAPI interface defines the contract for different drawing platforms.
    This is the 'Implementor' in the Bridge pattern.
    """
    
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        """
        Draw a circle at the specified coordinates with given radius.
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate  
            radius (float): Circle radius
            
        Returns:
            str: Description of the drawing operation
        """
        pass
    
    @abstractmethod
    def draw_rectangle(self, x: float, y: float, width: float, height: float) -> str:
        """
        Draw a rectangle at the specified coordinates with given dimensions.
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            width (float): Rectangle width
            height (float): Rectangle height
            
        Returns:
            str: Description of the drawing operation
        """
        pass
