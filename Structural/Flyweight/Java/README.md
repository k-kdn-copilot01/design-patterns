# Flyweight Design Pattern - Java Implementation

This folder contains Java implementations of the **Flyweight** design pattern, demonstrating different approaches and a real-world example.

## 📁 Folder Structure

- `Structure/`
  - `Main.java` — All structure classes in one file (104 lines)
- `Example/`
  - `Main.java` — All example classes in one file (110 lines)
- `README.md` — This documentation

## 🎯 When to Use Flyweight

The Flyweight pattern should be used when:
- You have a large number of similar objects
- You want to reduce memory usage by sharing common state
- You need to optimize performance for objects with shared characteristics
- You want to separate intrinsic (shared) state from extrinsic (unique) state
- You're dealing with objects that have expensive creation costs

## ⚖️ Intrinsic vs. Extrinsic State

### Intrinsic State (Shared)
```java
// Shared state that can be reused across multiple objects
private String intrinsicState;
```

**Characteristics:**
- Stored in the flyweight object
- Shared across multiple contexts
- Immutable
- Reduces memory usage

### Extrinsic State (Unique)
```java
// Unique state that varies per context
private String extrinsicState;
```

**Characteristics:**
- Passed to flyweight methods
- Unique per context
- Can be mutable
- Not stored in flyweight

### Real-World Example (`Example/Main.java`)
```java
// Character flyweight with shared formatting
public class ConcreteCharacterFlyweight {
    private char character; // Intrinsic state
    public void display(String font, int size, String color); // Extrinsic state
}
```

**Benefits:**
- Memory efficient for large text documents
- Shared formatting reduces memory usage
- Better performance for text rendering

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Structural/Flyweight/Java/Structure
   javac Main.java
   java Main
   ```

2. Demo example with structure classes:
   ```bash
   cd Structural/Flyweight/Java/Example
   javac Main.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
=== Structure Demo: Flyweight Implementations ===

1. Basic Flyweight:
FlyweightFactory: Creating new ConcreteFlyweight with key: A
ConcreteFlyweight created with intrinsic state: A
ConcreteFlyweight: Operation with extrinsic state: State1
FlyweightFactory: Reusing existing ConcreteFlyweight with key: A
ConcreteFlyweight: Operation with extrinsic state: State2

2. Multiple Flyweights:
FlyweightFactory: Creating new ConcreteFlyweight with key: B
ConcreteFlyweight created with intrinsic state: B
ConcreteFlyweight: Operation with extrinsic state: State3

Total flyweights created: 2

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)
```
=== Flyweight Design Pattern Demo ===

1. Testing Character Flyweight:
CharacterFlyweightFactory: Creating new CharacterFlyweight with key: H
ConcreteCharacterFlyweight created for character: H
Character H: Displaying with font: Arial, size: 12, color: Black
CharacterFlyweightFactory: Reusing existing CharacterFlyweight with key: H
Character H: Displaying with font: Arial, size: 12, color: Black

2. Testing Multiple Characters:
CharacterFlyweightFactory: Creating new CharacterFlyweight with key: e
ConcreteCharacterFlyweight created for character: e
Character e: Displaying with font: Arial, size: 12, color: Black

Total unique characters created: 2

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Memory Efficiency**: Shared intrinsic state reduces memory usage
2. **Factory Pattern**: FlyweightFactory manages flyweight creation and reuse
3. **State Separation**: Intrinsic (shared) vs Extrinsic (unique) state
4. **Performance**: Reduced object creation improves performance

## 🔍 Best Practices

- Use **Flyweight** for objects with shared intrinsic state
- Use **Factory** to manage flyweight creation and caching
- Separate **intrinsic** (shared) from **extrinsic** (unique) state
- Consider **thread safety** when sharing flyweights
- Use **immutable** intrinsic state for better performance

## 📋 File Structure Details

### Structure/Main.java (104 lines)
- **Flyweight Interface** (lines 1-8): Common interface for all flyweights
- **ConcreteFlyweight Class** (lines 10-32): Concrete flyweight with intrinsic state
- **FlyweightFactory Class** (lines 34-50): Factory managing flyweight creation
- **Client Class** (lines 52-68): Client using flyweights
- **Main Class** (lines 70-104): Demo implementation

### Example/Main.java (110 lines)
- **CharacterFlyweight Interface** (lines 1-8): Interface for character flyweights
- **ConcreteCharacterFlyweight Class** (lines 10-32): Character flyweight implementation
- **CharacterFlyweightFactory Class** (lines 34-50): Factory managing character flyweights
- **TextEditor Class** (lines 52-68): Text editor using character flyweights
- **Main Class** (lines 70-110): Real-world demo
