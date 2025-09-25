"""
Bridge Pattern - Real World Example Demo
Demonstrates the Bridge pattern with a drawing application scenario.
"""

from Circle import Circle
from Rectangle import Rectangle
from OpenGLAPI import OpenGLAPI
from DirectXAPI import DirectXAPI


def main():
    """
    Demo function showing the Bridge pattern in a real-world scenario.
    """
    print("=== Bridge Pattern Real-World Example Demo ===\n")
    print("Drawing Application: Shapes with Different Rendering APIs\n")
    
    # Create different drawing APIs
    opengl_api = OpenGLAPI()
    directx_api = DirectXAPI()
    
    print("1. Creating shapes with OpenGL API:")
    print("-" * 40)
    
    # Create shapes with OpenGL API
    circle_opengl = Circle(10, 20, 5, opengl_api)
    rectangle_opengl = Rectangle(0, 0, 10, 8, opengl_api)
    
    print(f"Created: {circle_opengl.get_info()}")
    print(f"Created: {rectangle_opengl.get_info()}")
    print()
    
    print("Drawing with OpenGL:")
    print(circle_opengl.draw())
    print(rectangle_opengl.draw())
    print()
    
    print("2. Creating shapes with DirectX API:")
    print("-" * 40)
    
    # Create shapes with DirectX API
    circle_directx = Circle(15, 25, 7, directx_api)
    rectangle_directx = Rectangle(5, 5, 12, 10, directx_api)
    
    print(f"Created: {circle_directx.get_info()}")
    print(f"Created: {rectangle_directx.get_info()}")
    print()
    
    print("Drawing with DirectX:")
    print(circle_directx.draw())
    print(rectangle_directx.draw())
    print()
    
    print("3. Demonstrating shape operations:")
    print("-" * 40)
    
    # Demonstrate resize operations
    print("Resizing shapes:")
    print(circle_opengl.resize(2.0))
    print(rectangle_directx.resize(1.5))
    print()
    
    print("Redrawing resized shapes:")
    print(circle_opengl.draw())
    print(rectangle_directx.draw())
    print()
    
    print("4. Switching APIs dynamically:")
    print("-" * 40)
    
    # Create a shape and show how we can use different APIs
    print("Same circle shape, different rendering APIs:")
    circle_gl = Circle(0, 0, 3, opengl_api)
    circle_dx = Circle(0, 0, 3, directx_api)
    
    print("OpenGL version:")
    print(circle_gl.draw())
    print()
    print("DirectX version:")
    print(circle_dx.draw())
    print()
    
    print("=== Bridge Pattern Real-World Example Demo Complete ===")


if __name__ == "__main__":
    main()
