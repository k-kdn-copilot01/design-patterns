# Prototype Design Pattern

This folder contains implementations of the **Prototype** design pattern in multiple programming languages, demonstrating both structural components and real-world examples.

## 📁 Folder Structure

- `Java/`
  - `Structure/`
    - `Prototype.java` — Base interface defining the clone contract
    - `ConcretePrototypeA.java` — Shallow cloning implementation
    - `ConcretePrototypeB.java` — Deep cloning implementation
    - `Client.java` — Client that uses prototypes for object creation
    - `Main.java` — Demo for structure-only implementations
  - `Example/`
    - `Document.java` — Real-world document cloning example
    - `DocumentMetadata.java` — Nested object for deep cloning demonstration
    - `Shape.java` — Abstract shape prototype
    - `Circle.java` — Concrete circle implementation
    - `Rectangle.java` — Concrete rectangle implementation
    - `PrototypeManager.java` — Prototype registry and factory
    - `Main.java` — Demo using real-world examples
- `Php/`
  - `Structure/` — Same structure as Java but in PHP
  - `Example/` — Same examples as Java but in PHP
- `README.md` — This documentation

## 🎯 When to Use Prototype

The Prototype pattern should be used when:
- Object creation is **expensive** (complex initialization, database queries, file operations)
- You need to create objects that are **similar to existing objects**
- You want to avoid subclasses of objects just to create similar objects
- Objects have **many possible configurations** and you want to avoid complex creation logic
- You need to create objects at **runtime** without knowing their classes beforehand

## 🔄 Shallow vs. Deep Cloning

### Shallow Clone (`ConcretePrototypeA`)
- **Primitive fields** are copied
- **Object references** are shared between original and clone
- Faster but changes to shared objects affect both instances

### Deep Clone (`ConcretePrototypeB`)
- **All fields** are copied, including nested objects
- Creates **completely independent** objects
- Slower but provides true isolation between instances

## 🚀 How to Run

### Java

1. Demo structure implementations only:
   ```bash
   cd Creational/Prototype/Java/Structure
   javac *.java
   java Main
   ```

2. Demo real-world examples:
   ```bash
   cd Creational/Prototype/Java/Example
   javac *.java
   java Main
   ```

### PHP

1. Demo structure implementations only:
   ```bash
   cd Creational/Prototype/Php/Structure
   php Main.php
   ```

2. Demo real-world examples:
   ```bash
   cd Creational/Prototype/Php/Example
   php Main.php
   ```

## 📊 Expected Output (Structure)

```
=== Structure Demo: Prototype Pattern ===

1. Shallow Clone Demonstration:
ConcretePrototypeA created: OriginalA
Original: ConcretePrototypeA[name=OriginalA, value=100, data=Initial data for OriginalA]
ConcretePrototypeA cloned: OriginalA (Clone)
Clone: ConcretePrototypeA[name=OriginalA (Clone), value=100, data=Initial data for OriginalA]
originalA == cloneA: false
After modifying original:
Original: ConcretePrototypeA[name=OriginalA, value=100, data=Initial data for OriginalA - Modified by original]
Clone: ConcretePrototypeA[name=OriginalA (Clone), value=100, data=Initial data for OriginalA - Modified by original] (affected by shallow copy)

2. Deep Clone Demonstration:
ConcretePrototypeB created: OriginalB
Original: ConcretePrototypeB[name=OriginalB, value=200, data=Initial data for OriginalB]
ConcretePrototypeB deep cloned: OriginalB (Deep Clone)
Clone: ConcretePrototypeB[name=OriginalB (Deep Clone), value=200, data=Initial data for OriginalB]
originalB == cloneB: false
After modifying original:
Original: ConcretePrototypeB[name=OriginalB, value=200, data=Initial data for OriginalB - Modified by original]
Clone: ConcretePrototypeB[name=OriginalB (Deep Clone), value=200, data=Initial data for OriginalB] (independent due to deep copy)

3. Client Usage Demonstration:
Client prototype: ConcretePrototypeA[name=OriginalA, value=100, data=Initial data for OriginalA - Modified by original]
Created object 1: ConcretePrototypeA[name=OriginalA (Clone), value=100, data=Initial data for OriginalA - Modified by original]
Created object 2: ConcretePrototypeA[name=OriginalA (Clone), value=100, data=Initial data for OriginalA - Modified by original]
newObject1 == newObject2: false

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example)

```
=== Example Demo: Prototype Pattern Real-World Usage ===

1. Document Cloning Scenario:
Document created: Project Proposal
Original: Document[title='Project Proposal', author='John Doe', tags=["important","project"], Metadata[version=1, status='Review', created=2025-09-13 03:51:45]]
Document cloned: Project Proposal (Copy)
Edited Copy: Document[title='Project Proposal (Copy)', author='John Doe', tags=["important","project","modified"], Metadata[version=2, status='Review', created=2025-09-13 03:51:45]]
Original after cloning: Document[title='Project Proposal', author='John Doe', tags=["important","project"], Metadata[version=1, status='Review', created=2025-09-13 03:51:45]]
Independent copies: true
Different versions: true

2. Shape Cloning Scenario:
Circle created: radius=5, color=red
Rectangle created: 4x6, color=blue
Original Circle: Circle[radius=5.0, color='red', position=(10,20), area=78.54]
Original Rectangle: Rectangle[width=4.0, height=6.0, color='blue', position=(0,0), area=24.00]

After modifying clones:
Original Circle: Circle[radius=5.0, color='red', position=(10,20), area=78.54]
Cloned Circle: Circle[radius=8.0, color='green', position=(50,60), area=201.06]
Original Rectangle: Rectangle[width=4.0, height=6.0, color='blue', position=(0,0), area=24.00]
Cloned Rectangle: Rectangle[width=8.0, height=3.0, color='yellow', position=(100,200), area=24.00]

3. Prototype Manager Usage:
Prototype registered: standard-circle
New Circle: Circle[radius=5.0, color='red', position=(10,20), area=78.54]
New Rectangle: Rectangle[width=4.0, height=6.0, color='blue', position=(0,0), area=24.00]
Objects are independent: true

=== Example Demo Complete ===
```

## 🎓 Key Learning Points

1. **Object Independence**: `original != clone` proves that cloning creates new instances
2. **Shallow vs Deep**: Notice how shared references behave differently in shallow vs deep cloning
3. **Performance**: Cloning can be faster than construction when initialization is expensive
4. **Registry Pattern**: PrototypeManager shows how to manage multiple prototype templates
5. **Flexibility**: Easy to create variations of objects without knowing their exact types

## 💡 Real-World Use Cases

- **Document Templates**: Clone document templates and customize content
- **Game Objects**: Clone enemy units, weapons, or terrain pieces
- **Configuration Objects**: Clone application settings for different environments
- **UI Components**: Clone widget configurations in graphical applications
- **Database Records**: Clone database entities for batch operations

## 🔍 Best Practices

- Use **Deep Clone** when you need complete independence between objects
- Use **Shallow Clone** when shared references are acceptable and performance is critical
- Implement a **Prototype Manager** for complex applications with many prototype types
- Always test cloning behavior with nested objects to ensure expected independence
- Consider using libraries or built-in cloning mechanisms in production code
- Be careful with **circular references** in deep cloning scenarios