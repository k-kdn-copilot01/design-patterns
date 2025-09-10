# Prototype Design Pattern

This folder contains implementations of the **Prototype** design pattern in multiple programming languages, demonstrating both structural components and real-world examples.

## 📁 Folder Structure

- `Java/` — Java implementation with Structure and Example demos
- `Php/` — PHP implementation with Structure and Example demos

Each language folder contains:
- `Structure/` — Core pattern components (Prototype interface, ConcretePrototypes, Client)
- `Example/` — Real-world scenario using geometric shapes
- `README.md` — Language-specific documentation

## 🎯 Pattern Overview

The **Prototype pattern** lets you copy existing objects without making your code dependent on their classes. It delegates the cloning process to the actual objects that are being cloned.

### Key Components:
- **Prototype** — Interface declaring the clone method
- **ConcretePrototype** — Classes that implement the cloning method
- **Client** — Creates new objects by asking prototypes to clone themselves

## 🔧 Use Cases

- **Configuration Objects**: Clone base configurations and modify specific settings
- **Game Development**: Clone enemy units, weapons, or levels with variations
- **Graphics Editors**: Clone shapes, images, or drawing elements
- **Database Records**: Clone record templates with different data
- **Complex Object Creation**: Avoid expensive initialization by cloning

## 🚀 Quick Start

**Java:**
```bash
# Structure demo
cd Java/Structure && javac *.java && java Main

# Real-world example
cd ../Example && javac *.java && java Main
```

**PHP:**
```bash
# Structure demo
cd Php/Structure && php Main.php

# Real-world example
cd ../Example && php Main.php
```

## 🎓 Key Benefits

1. **Performance**: Faster than creating complex objects from scratch
2. **Flexibility**: Create objects without knowing their concrete classes
3. **Reduced Coupling**: Client code doesn't depend on specific constructors
4. **Runtime Configuration**: Specify object types at runtime
5. **Simplified Creation**: Clone complex objects easily

## 📚 Learning Resources

- [Refactoring Guru - Prototype Pattern](https://refactoring.guru/design-patterns/prototype)
- Language-specific README files in each folder
- Working code examples with detailed comments