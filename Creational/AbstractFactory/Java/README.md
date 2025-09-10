# Abstract Factory Design Pattern - Java Implementation

This folder contains Java implementations of the **Abstract Factory** design pattern, demonstrating both basic structure and a real-world UI toolkit example.

## 📁 Folder Structure

- `Structure/`
  - `AbstractFactory.java` — Abstract factory interface
  - `ConcreteFactory1.java` / `ConcreteFactory2.java` — Concrete factory implementations
  - `ProductA.java` / `ProductB.java` — Abstract product interfaces
  - `ConcreteProductA1.java` / `ConcreteProductA2.java` — Concrete product A implementations
  - `ConcreteProductB1.java` / `ConcreteProductB2.java` — Concrete product B implementations
  - `Client.java` — Client that uses abstract factory
  - `Main.java` — Demo for structure-only implementations
- `Example/`
  - `UIFactory.java` — Abstract UI factory interface
  - `WinFactory.java` / `MacFactory.java` — Platform-specific UI factories
  - `Button.java` / `Checkbox.java` — Abstract UI component interfaces
  - `WinButton.java` / `MacButton.java` — Windows/Mac button implementations
  - `WinCheckbox.java` / `MacCheckbox.java` — Windows/Mac checkbox implementations
  - `Application.java` — Client application using UI components
  - `Main.java` — Demo using UI toolkit with real-world scenario
- `README.md` — This documentation

## 🎯 When to Use Abstract Factory

The Abstract Factory pattern should be used when:
- You need to create **families of related products** without specifying their concrete classes
- Your system should be independent of how its products are created, composed, and represented
- You want to provide a class library of products, revealing only their interfaces
- You need to ensure that products from the same family are used together

## 🏗️ Pattern Components

### Core Structure
- **AbstractFactory**: Interface declaring methods for creating abstract products
- **ConcreteFactory**: Implements creation methods for specific product families
- **AbstractProduct**: Interface for each type of product
- **ConcreteProduct**: Specific implementations of products for each family
- **Client**: Uses only AbstractFactory and AbstractProduct interfaces

### UI Toolkit Example
- **UIFactory**: Abstract factory for creating UI components
- **WinFactory/MacFactory**: Platform-specific factories creating Windows/Mac styled components
- **Button/Checkbox**: Abstract UI component interfaces
- **WinButton/MacButton, WinCheckbox/MacCheckbox**: Platform-specific implementations
- **Application**: Client that creates and uses UI components through the factory

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Creational/AbstractFactory/Java/Structure
   javac *.java
   java Main
   ```

2. Demo example with UI toolkit:
   ```bash
   cd Creational/AbstractFactory/Java/Example
   javac *.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
=== Structure Demo: Abstract Factory Pattern ===

1. Using ConcreteFactory1:
Client: Creating products using ConcreteFactory1
ConcreteProductA1: Operation A executed
ConcreteProductB1: Operation B executed
ConcreteProductB1: Collaborating with ConcreteProductA1

2. Using ConcreteFactory2:
Client: Creating products using ConcreteFactory2
ConcreteProductA2: Operation A executed
ConcreteProductB2: Operation B executed
ConcreteProductB2: Collaborating with ConcreteProductA2

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)
```
=== Example Demo: UI Toolkit Abstract Factory ===

1. Creating Windows Application:
Application: Rendering UI using WinFactory
Rendering Windows-style button [Submit]
Rendering Windows-style checkbox [ ] Remember me

Application: Simulating user interaction...
Windows button clicked with Windows event handling
Windows checkbox toggled to: checked
Checkbox state: checked

2. Creating Mac Application:
Application: Rendering UI using MacFactory
Rendering Mac-style button (Submit)
Rendering Mac-style checkbox ( ) Remember me

Application: Simulating user interaction...
Mac button clicked with Cocoa event handling
Mac checkbox toggled to: checked
Checkbox state: checked

=== Example Demo Complete ===
```

## 🎓 Key Learning Points

1. **Family Creation**: Each factory creates a complete family of compatible products
2. **Consistent Products**: Products from the same factory are designed to work together
3. **Easy Switching**: Changing the factory switches the entire product family
4. **Isolation**: Client code doesn't depend on concrete product classes
5. **Extensibility**: Adding new product families requires only new factory and product classes

## 🔍 Advantages

- **Isolation of concrete classes**: Client code uses products through abstract interfaces
- **Easy product family switching**: Change factory to get different product family
- **Consistency among products**: Products from one factory are designed to work together
- **Support for new families**: Adding new product families is relatively easy

## ⚠️ Disadvantages

- **Complexity**: More classes and interfaces to maintain
- **Difficult to add new products**: Adding new product types requires changing all factory interfaces
- **Runtime overhead**: Extra level of indirection through factory interface

## 💡 Real-World Use Cases

- **Cross-platform UI frameworks** (Swing, Qt, GTK)
- **Database drivers** (MySQL, PostgreSQL, Oracle drivers)
- **Game engines** (different renderers for DirectX, OpenGL, Vulkan)
- **Operating system abstraction layers**
- **Document creation libraries** (PDF, Word, Excel generators)