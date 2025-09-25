"""
Main: Demonstrates the Decorator pattern with a real-world text formatting example.
"""
from PlainText import PlainText
from BoldDecorator import BoldDecorator
from ItalicDecorator import ItalicDecorator
from UnderlineDecorator import UnderlineDecorator
from ColorDecorator import ColorDecorator


def main():
    """Demonstrate the Decorator pattern with text formatting."""
    print("=== Text Formatting with Decorator Pattern ===\n")
    
    # Create a plain text
    text = PlainText("Hello, World!")
    print(f"1. Plain text: {text.format()}")
    print(f"   Plain text content: '{text.get_plain_text()}'\n")
    
    # Add bold formatting
    bold_text = BoldDecorator(text)
    print(f"2. Bold text: {bold_text.format()}")
    print(f"   Plain text content: '{bold_text.get_plain_text()}'\n")
    
    # Add italic formatting
    italic_text = ItalicDecorator(text)
    print(f"3. Italic text: {italic_text.format()}")
    print(f"   Plain text content: '{italic_text.get_plain_text()}'\n")
    
    # Add underline formatting
    underline_text = UnderlineDecorator(text)
    print(f"4. Underlined text: {underline_text.format()}")
    print(f"   Plain text content: '{underline_text.get_plain_text()}'\n")
    
    # Add color formatting
    red_text = ColorDecorator(text, "red")
    print(f"5. Red text: {red_text.format()}")
    print(f"   Plain text content: '{red_text.get_plain_text()}'\n")
    
    # Combine multiple decorators
    print("=== Combining Multiple Decorators ===")
    
    # Bold + Italic
    bold_italic = ItalicDecorator(BoldDecorator(text))
    print(f"6. Bold + Italic: {bold_italic.format()}")
    
    # Bold + Italic + Underline
    bold_italic_underline = UnderlineDecorator(ItalicDecorator(BoldDecorator(text)))
    print(f"7. Bold + Italic + Underline: {bold_italic_underline.format()}")
    
    # Color + Bold + Italic
    colored_bold_italic = ItalicDecorator(BoldDecorator(ColorDecorator(text, "blue")))
    print(f"8. Blue + Bold + Italic: {colored_bold_italic.format()}")
    
    # Complex combination
    complex_formatting = UnderlineDecorator(
        ItalicDecorator(
            BoldDecorator(
                ColorDecorator(text, "green")
            )
        )
    )
    print(f"9. Green + Bold + Italic + Underline: {complex_formatting.format()}")
    
    print("\n=== Real-world Benefits ===")
    print("- Dynamic text formatting without modifying existing classes")
    print("- Flexible combination of formatting features")
    print("- Easy to add new formatting types (just create new decorators)")
    print("- Maintains original text content while adding visual formatting")
    print("- Each decorator has a single responsibility")
    
    print("\n=== Usage in Applications ===")
    print("- Rich text editors")
    print("- Markdown processors")
    print("- HTML generators")
    print("- Document formatting systems")
    print("- UI component styling")


if __name__ == "__main__":
    main()
