"""
Bridge Pattern - Example Package
Real-world example implementation of the Bridge pattern.
"""

from .DrawingAPI import DrawingAPI
from .OpenGLAPI import OpenGLAPI
from .DirectXAPI import DirectXAPI
from .Shape import Shape
from .Circle import Circle
from .Rectangle import Rectangle

__all__ = [
    'DrawingAPI',
    'OpenGLAPI',
    'DirectXAPI', 
    'Shape',
    'Circle',
    'Rectangle'
]
