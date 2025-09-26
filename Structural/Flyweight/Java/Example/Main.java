/**
 * Character Flyweight Interface
 * 
 * This interface defines the common operations for character flyweights.
 */
interface CharacterFlyweight {
    void display(String font, int size, String color);
}

/**
 * Concrete Character Flyweight
 * 
 * This represents a character with shared intrinsic state (the character itself)
 * and extrinsic state (formatting) passed during display.
 */
class ConcreteCharacterFlyweight implements CharacterFlyweight {
    private char character;
    
    public ConcreteCharacterFlyweight(char character) {
        this.character = character;
        System.out.println("ConcreteCharacterFlyweight created for character: " + character);
    }
    
    @Override
    public void display(String font, int size, String color) {
        System.out.println("Character " + character + ": Displaying with font: " + font + 
                          ", size: " + size + ", color: " + color);
    }
    
    public char getCharacter() {
        return character;
    }
}

/**
 * Character Flyweight Factory
 * 
 * This factory manages the creation and caching of character flyweights.
 * It ensures that characters with the same intrinsic state are reused.
 */
class CharacterFlyweightFactory {
    private java.util.Map<Character, CharacterFlyweight> characters = new java.util.HashMap<>();
    
    public CharacterFlyweight getCharacter(char character) {
        if (characters.containsKey(character)) {
            System.out.println("CharacterFlyweightFactory: Reusing existing CharacterFlyweight with key: " + character);
            return characters.get(character);
        } else {
            System.out.println("CharacterFlyweightFactory: Creating new CharacterFlyweight with key: " + character);
            ConcreteCharacterFlyweight flyweight = new ConcreteCharacterFlyweight(character);
            characters.put(character, flyweight);
            return flyweight;
        }
    }
    
    public int getCharacterCount() {
        return characters.size();
    }
}

/**
 * Text Editor Class
 * 
 * This class demonstrates how to use character flyweights in a text editor.
 */
class TextEditor {
    private CharacterFlyweightFactory factory;
    
    public TextEditor() {
        this.factory = new CharacterFlyweightFactory();
    }
    
    public void displayText(String text, String font, int size, String color) {
        System.out.println("Displaying text: \"" + text + "\"");
        for (char c : text.toCharArray()) {
            CharacterFlyweight character = factory.getCharacter(c);
            character.display(font, size, color);
        }
    }
    
    public int getCharacterCount() {
        return factory.getCharacterCount();
    }
}

/**
 * Main class to demonstrate Character Flyweight pattern
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Flyweight Design Pattern Demo ===\n");
        
        // Test Character Flyweight with text
        System.out.println("1. Testing Character Flyweight:");
        TextEditor editor = new TextEditor();
        
        System.out.println("Displaying 'Hello' with Arial font:");
        editor.displayText("Hello", "Arial", 12, "Black");
        
        System.out.println("\nDisplaying 'World' with Times font:");
        editor.displayText("World", "Times", 14, "Blue");
        
        System.out.println("\nDisplaying 'Hello World' with Calibri font:");
        editor.displayText("Hello World", "Calibri", 16, "Red");
        
        System.out.println("\nTotal unique characters created: " + editor.getCharacterCount());
        System.out.println("\n=== Demo Complete ===");
    }
}
