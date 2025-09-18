# Abstract Factory Design Pattern - Python Implementation

This folder contains Python implementations of the **Abstract Factory** design pattern, demonstrating the core structure and a real-world GUI theming example.

## 📁 Folder Structure

- `Structure/`
  - `abstract_factory.py` — Abstract factory and product interfaces
  - `concrete_factories.py` — Concrete factories and products (ConcreteFactory1/2)
  - `client.py` — Client code that works with abstract interfaces
  - `main.py` — Demo for structure-only implementations
- `Example/`
  - `gui_factory.py` — Abstract GUI factory and component interfaces
  - `windows_factory.py` — Windows-themed GUI components factory
  - `macos_factory.py` — MacOS-themed GUI components factory
  - `application.py` — Application that uses GUI factories
  - `main.py` — Real-world demo with GUI theming
- `README.md` — This documentation

## 🎯 When to Use Abstract Factory

The Abstract Factory pattern should be used when:
- You need to create **families of related products** that work together
- You want to ensure products from the same family are **compatible** with each other
- You need to **switch between different product families** at runtime
- You want to **decouple** client code from concrete product classes
- Your system should be **configured with multiple families** of products

## 🏗️ Pattern Structure

### Core Components

1. **Abstract Factory** (`AbstractFactory`)
   - Declares creation methods for each product type
   - Returns abstract product types

2. **Concrete Factories** (`ConcreteFactory1`, `ConcreteFactory2`)
   - Implement creation methods to produce concrete products
   - Each factory creates products belonging to a single family

3. **Abstract Products** (`AbstractProductA`, `AbstractProductB`)
   - Declare interfaces for different product types
   - Define contracts that concrete products must follow

4. **Concrete Products** (`ConcreteProductA1`, `ConcreteProductB1`)
   - Implement abstract product interfaces
   - Products from the same family are designed to work together

5. **Client** (`Client`)
   - Works only with abstract factories and products
   - Remains independent of concrete product classes

## 🔄 How It Works

```python
# 1. Client receives a factory instance
factory = ConcreteFactory1()  # or ConcreteFactory2()

# 2. Client creates products using the factory
product_a = factory.create_product_a()
product_b = factory.create_product_b()

# 3. Products from the same family work together
result = product_b.collaborate_with(product_a)
```

## 🚀 How to Run

### Structure Demo (Core Pattern)
```bash
cd Creational/AbstractFactory/Python/Structure
python main.py
```

### Example Demo (GUI Theming)
```bash
cd Creational/AbstractFactory/Python/Example
python main.py
```

## 📊 Expected Output (Structure/main.py)

```
=== Structure Demo: Abstract Factory Pattern ===

1. Using ConcreteFactory1:
The result of the product B1.
The result of the B1 collaborating with the (The result of the product A1.)

2. Using ConcreteFactory2:
The result of the product B2.
The result of the B2 collaborating with the (The result of the product A2.)

3. Using Client class with different factories:
Client: Working with ConcreteFactory1
Product A: The result of the product A1.
Product B: The result of the product B1.
Collaboration: The result of the B1 collaborating with the (The result of the product A1.)

Client: Working with ConcreteFactory2
Product A: The result of the product A2.
Product B: The result of the product B2.
Collaboration: The result of the B2 collaborating with the (The result of the product A2.)

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/main.py)

```
=== Abstract Factory Pattern - GUI Themes Example ===

=== Direct Factory Usage Demo ===

1. Creating Windows-themed application:
Factory: WindowsFactory
  Window: Rendering Windows-style window with title bar and minimize/maximize/close buttons
  Button: Rendering Windows-style button with rectangular borders
  Checkbox: Rendering Windows-style checkbox: ☐ (square design)

User Interactions:
  Windows button clicked with system sound
  Windows checkbox toggled to checked
  Updated checkbox: Rendering Windows-style checkbox: ☑ (square design)
  Windows window closed with fade animation

2. Creating MacOS-themed application:
Factory: MacOSFactory
  Window: Rendering MacOS-style window with traffic light buttons (red, yellow, green)
  Button: Rendering MacOS-style button with rounded corners and gradient
  Checkbox: Rendering MacOS-style checkbox: ○ (circular design)

User Interactions:
  MacOS button clicked with elegant haptic feedback
  MacOS checkbox smoothly animated to checked
  Updated checkbox: Rendering MacOS-style checkbox: ✓ (circular design)
  MacOS window closed with smooth scaling animation

=== Runtime Configuration Demo ===

Detected OS: Windows
Factory: WindowsFactory
  Window: Rendering Windows-style window with title bar and minimize/maximize/close buttons
  Button: Rendering Windows-style button with rectangular borders
  Checkbox: Rendering Windows-style checkbox: ☐ (square design)

User Interactions:
  Windows button clicked with system sound
  Windows checkbox toggled to checked
  Updated checkbox: Rendering Windows-style checkbox: ☑ (square design)
  Windows window closed with fade animation

Detected OS: MacOS
Factory: MacOSFactory
  Window: Rendering MacOS-style window with traffic light buttons (red, yellow, green)
  Button: Rendering MacOS-style button with rounded corners and gradient
  Checkbox: Rendering MacOS-style checkbox: ○ (circular design)

User Interactions:
  MacOS button clicked with elegant haptic feedback
  MacOS checkbox smoothly animated to checked
  Updated checkbox: Rendering MacOS-style checkbox: ✓ (circular design)
  MacOS window closed with smooth scaling animation

=== Product Family Compatibility Demo ===

Mixing products from different families would break compatibility!
Abstract Factory ensures products from the same family work together.

Windows family - all components have consistent styling:
  Rendering Windows-style button with rectangular borders
  Rendering Windows-style checkbox: ☐ (square design)
  Rendering Windows-style window with title bar and minimize/maximize/close buttons

MacOS family - all components have consistent styling:
  Rendering MacOS-style button with rounded corners and gradient
  Rendering MacOS-style checkbox: ○ (circular design)
  Rendering MacOS-style window with traffic light buttons (red, yellow, green)

=== Example Demo Complete ===
```

## 🎓 Key Learning Points

### 1. **Product Family Consistency**
- All products created by the same factory work together seamlessly
- Windows factory creates Windows-themed button, checkbox, and window
- MacOS factory creates MacOS-themed components with consistent styling

### 2. **Runtime Flexibility**
- Application can switch between different themes without code changes
- Factory selection determines the entire product family used

### 3. **Decoupling**
- Client code (`Application`) doesn't know about concrete factories
- Adding new themes requires only new factory implementations

### 4. **Guaranteed Compatibility**
- Abstract Factory ensures products from the same family are compatible
- Prevents mixing incompatible products (e.g., Windows button with MacOS window)

## 🆚 Abstract Factory vs Factory Method

| Aspect | Abstract Factory | Factory Method |
|--------|------------------|----------------|
| **Scope** | Creates families of related products | Creates single products |
| **Interface** | Multiple creation methods | Single creation method |
| **Products** | Multiple product types | One product type |
| **Complexity** | More complex structure | Simpler structure |
| **Use Case** | GUI themes, cross-platform libraries | Single product variations |

## 🔍 Real-World Applications

1. **GUI Frameworks**
   - Cross-platform UI libraries (Qt, GTK)
   - Web component libraries with themes

2. **Gaming**
   - Character families (warrior, mage, archer)
   - Environment sets (forest, desert, snow)

3. **Document Processing**
   - Export formats (PDF, HTML, XML)
   - Template families (business, academic, creative)

4. **Database Drivers**
   - Different database families (MySQL, PostgreSQL, SQLite)
   - Connection, statement, and result set families

## ⚡ Best Practices

1. **Use when you have multiple related products** that should work together
2. **Start with Factory Method** if you only need single product creation
3. **Consider the maintenance overhead** - more complex than simple factories
4. **Document product family relationships** clearly
5. **Use dependency injection** to provide factories to clients
6. **Keep abstract interfaces stable** to avoid breaking client code

## ⚠️ Common Pitfalls

- **Over-engineering**: Don't use Abstract Factory for single products
- **Rigid hierarchies**: Hard to add new product types to existing families
- **Complex configuration**: Managing multiple factories can be challenging
- **Memory overhead**: Creating multiple product types even when not all are needed
