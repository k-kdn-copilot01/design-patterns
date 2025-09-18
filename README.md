# Design Patterns Samples

This repository contains sample source code implementations of various **design patterns**.  
The purpose is to provide a clean and practical reference for developers who want to understand how design patterns can be applied in real projects.

> All examples are organized by **categories** → **design patterns** → **programming languages**.

---

## 📂 Repository Structure

```
.
├── Creational/              # Khởi tạo (Creational Patterns)
│   ├── Singleton/
│   │   ├── Java/
│   │   ├── Php/
│   │   └── Python/
│   ├── FactoryMethod/
│   └── AbstractFactory/
│
├── Structural/              # Cấu trúc (Structural Patterns)
│   ├── Adapter/
│   ├── Decorator/
│   └── Proxy/
│
└── Behavioral/              # Hành vi (Behavioral Patterns)
    ├── Observer/
    ├── Strategy/
    └── Command/
````
---

## 📖 Patterns Included

### Creational
| Pattern | Link |
|---------|------|
| Singleton | [View Code](./Creational/Singleton) |
| Factory Method | [View Code](./Creational/FactoryMethod) |
| Abstract Factory | [View Code](./Creational/AbstractFactory) |
| Builder | [View Code](./Creational/Builder) |
| Prototype | [View Code](./Creational/Prototype) |

### Structural
| Pattern | Link |
|---------|------|
| Adapter | [View Code](./Structural/Adapter) |
| Bridge | [View Code](./Structural/Bridge) |
| Composite | [View Code](./Structural/Composite) |
| Decorator | [View Code](./Structural/Decorator) |
| Facade | [View Code](./Structural/Facade) |
| Flyweight | [View Code](./Structural/Flyweight) |
| Proxy | [View Code](./Structural/Proxy) |

### Behavioral
| Pattern | Link |
|---------|------|
| Chain of Responsibility | [View Code](./Behavioral/ChainOfResponsibility) |
| Command | [View Code](./Behavioral/Command) |
| Iterator | [View Code](./Behavioral/Iterator) |
| Mediator | [View Code](./Behavioral/Mediator) |
| Memento | [View Code](./Behavioral/Memento) |
| Observer | [View Code](./Behavioral/Observer) |
| State | [View Code](./Behavioral/State) |
| Strategy | [View Code](./Behavioral/Strategy) |
| Template Method | [View Code](./Behavioral/TemplateMethod) |
| Visitor | [View Code](./Behavioral/Visitor) |

> Each folder contains subfolders for supported programming languages (e.g., `Java`, `Php`, ...).  

---

## 🚀 Usage

1. Navigate to the pattern folder you want to study.  
2. Choose the programming language (e.g., `Java`, `Php`).  
3. Open the source code files.  
4. Compile and run them locally.

Examples:

**Java:**
```bash
# Structure demo (basic implementations)
cd Creational/Singleton/Java/Structure
javac *.java
java Main

# Example demo (real-world example)
cd ../Example
javac ../Structure/*.java *.java
java Main
```

**PHP:**
```bash
# Structure demo (basic implementations)
cd Creational/Singleton/Php/Structure
php Main.php

# Example demo (real-world example)
cd ../Example
php Main.php
```

**Python:**
```bash
# Structure demo (basic implementations)
cd Creational/Singleton/Python/Structure
python main.py

# Example demo (real-world example)
cd ../Example
python main.py

# Abstract Factory pattern
cd Creational/AbstractFactory/Python/Structure
python main.py

# Abstract Factory example (GUI themes)
cd ../Example
python main.py
```

---

## 📚 Reference

Concepts are based on [Refactoring.Guru – Design Patterns](https://refactoring.guru/design-patterns).
This repository **only provides source code samples**, not detailed explanations.

---

## 🤝 Contribution

You are welcome to contribute by:

* Adding new design pattern implementations
* Supporting more programming languages
* Improving code quality

---

## 📜 License

Released under the **MIT License**.
You can freely use, modify, and share the code with attribution.
