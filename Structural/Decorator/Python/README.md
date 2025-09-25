# Decorator Pattern - Python Implementation

## 📋 Overview

The **Decorator Pattern** is a structural design pattern that allows you to attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors. It provides a flexible alternative to subclassing for extending functionality.

## 🎯 Intent

- Attach additional responsibilities to an object dynamically
- Provide a flexible alternative to subclassing for extending functionality
- Keep the same interface while adding new behaviors

## 🏗️ Structure

```
Component (Abstract)
├── operation()
│
ConcreteComponent
├── operation() → "ConcreteComponent"
│
Decorator (Abstract)
├── _component: Component
├── operation() → delegates to _component
│
ConcreteDecoratorA
├── operation() → "ConcreteDecoratorA(" + component.operation() + ")"
│
ConcreteDecoratorB
└── operation() → "ConcreteDecoratorB(" + component.operation() + ")"
```

## 📁 Project Structure

```
Python/
├── Structure/           # Core pattern implementation
│   ├── Component.py           # Abstract base component
│   ├── ConcreteComponent.py   # Concrete component
│   ├── Decorator.py           # Base decorator
│   ├── ConcreteDecoratorA.py  # Concrete decorator A
│   ├── ConcreteDecoratorB.py  # Concrete decorator B
│   └── Main.py               # Structure demo
│
├── Example/             # Real-world example
│   ├── TextComponent.py       # Abstract text component
│   ├── PlainText.py          # Plain text implementation
│   ├── TextDecorator.py      # Base text decorator
│   ├── BoldDecorator.py      # Bold formatting
│   ├── ItalicDecorator.py    # Italic formatting
│   ├── UnderlineDecorator.py # Underline formatting
│   ├── ColorDecorator.py     # Color formatting
│   └── Main.py              # Example demo
│
└── README.md            # This file
```

## 🚀 How to Run

### Structure Demo (Core Pattern)

```bash
cd Structural/Decorator/Python/Structure
python Main.py
```

**Expected Output:**
```
=== Decorator Pattern Demo ===

1. Basic component: ConcreteComponent
2. With DecoratorA: ConcreteDecoratorA(ConcreteComponent)
3. With DecoratorB: ConcreteDecoratorB(ConcreteComponent)
4. With DecoratorA + DecoratorB: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
5. With DecoratorB + DecoratorA: ConcreteDecoratorA(ConcreteDecoratorB(ConcreteComponent))
6. With DecoratorA + DecoratorA: ConcreteDecoratorA(ConcreteDecoratorA(ConcreteComponent))

=== Pattern Benefits ===
- Dynamic behavior addition without altering existing code
- Flexible combination of behaviors
- Single Responsibility Principle compliance
- Open/Closed Principle compliance
```

### Example Demo (Text Formatting)

```bash
cd Structural/Decorator/Python/Example
python Main.py
```

**Expected Output:**
```
=== Text Formatting with Decorator Pattern ===

1. Plain text: Hello, World!
   Plain text content: 'Hello, World!'

2. Bold text: **Hello, World!**
   Plain text content: 'Hello, World!'

3. Italic text: *Hello, World!*
   Plain text content: 'Hello, World!'

4. Underlined text: <u>Hello, World!</u>
   Plain text content: 'Hello, World!'

5. Red text: <span style="color: red">Hello, World!</span>
   Plain text content: 'Hello, World!'

=== Combining Multiple Decorators ===
6. Bold + Italic: ***Hello, World!***
7. Bold + Italic + Underline: <u>***Hello, World!***</u>
8. Blue + Bold + Italic: ***<span style="color: blue">Hello, World!</span>***
9. Green + Bold + Italic + Underline: <u>***<span style="color: green">Hello, World!</span>***</u>

=== Real-world Benefits ===
- Dynamic text formatting without modifying existing classes
- Flexible combination of formatting features
- Easy to add new formatting types (just create new decorators)
- Maintains original text content while adding visual formatting
- Each decorator has a single responsibility

=== Usage in Applications ===
- Rich text editors
- Markdown processors
- HTML generators
- Document formatting systems
- UI component styling
```

## 🔧 Key Components

### Structure Implementation

1. **Component**: Abstract base class defining the interface
2. **ConcreteComponent**: Basic implementation without decorations
3. **Decorator**: Base decorator class that maintains component reference
4. **ConcreteDecoratorA/B**: Specific decorators adding behaviors

### Example Implementation

1. **TextComponent**: Abstract base for text formatting
2. **PlainText**: Basic text without formatting
3. **TextDecorator**: Base decorator for text formatting
4. **BoldDecorator**: Adds bold formatting (`**text**`)
5. **ItalicDecorator**: Adds italic formatting (`*text*`)
6. **UnderlineDecorator**: Adds underline formatting (`<u>text</u>`)
7. **ColorDecorator**: Adds color formatting (`<span style="color: color">text</span>`)

## ✅ Benefits

- **Flexibility**: Add/remove behaviors at runtime
- **Single Responsibility**: Each decorator has one specific behavior
- **Open/Closed Principle**: Open for extension, closed for modification
- **Composition over Inheritance**: Favor object composition
- **Dynamic Behavior**: Change object behavior without changing the class

## 🎯 Use Cases

- **Text Formatting**: Rich text editors, markdown processors
- **Stream Processing**: Adding compression, encryption, buffering
- **UI Components**: Adding borders, shadows, animations
- **I/O Operations**: Adding logging, caching, validation
- **Middleware**: Adding authentication, logging, error handling

## 🔄 Comparison with Other Patterns

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Decorator** | Add behaviors dynamically | Need to add features without changing existing code |
| **Adapter** | Make incompatible interfaces work together | Interface mismatch |
| **Facade** | Provide simplified interface | Complex subsystem |
| **Proxy** | Control access to object | Access control, lazy loading |

## 📚 Related Patterns

- **Adapter**: Both use composition, but Adapter changes interface
- **Composite**: Decorator can be used with Composite for tree structures
- **Strategy**: Decorator changes object's skin, Strategy changes its guts
- **Chain of Responsibility**: Decorator chains are fixed, CoR chains are dynamic

## 🧪 Testing the Implementation

Both demos can be run independently and demonstrate:

1. **Basic functionality**: Core pattern behavior
2. **Multiple decorations**: Combining different decorators
3. **Order dependency**: How decoration order affects output
4. **Real-world application**: Practical text formatting example

The implementations follow Python best practices with:
- Type hints for better code clarity
- Abstract base classes for interface definition
- Clear separation of concerns
- Comprehensive documentation
