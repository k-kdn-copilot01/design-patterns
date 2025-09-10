# Prototype Design Pattern - Java Implementation

This folder contains Java implementations of the **Prototype** design pattern, demonstrating different approaches and a real-world example.

## 📁 Folder Structure

- `Structure/`
  - `Prototype.java` — Interface declaring the clone method
  - `ConcretePrototypeA.java` — First concrete prototype implementation
  - `ConcretePrototypeB.java` — Second concrete prototype implementation  
  - `Client.java` — Client class that works with prototypes
  - `Main.java` — Demo for structure-only implementations
- `Example/`
  - `Shape.java` — Abstract shape prototype base class
  - `Circle.java` — Concrete circle shape that can be cloned
  - `Rectangle.java` — Concrete rectangle shape that can be cloned
  - `Main.java` — Real-world example using geometric shapes
- `README.md` — This documentation

## 🎯 When to Use Prototype

The Prototype pattern should be used when:
- You need to **clone objects** without knowing their concrete types
- Creating new instances is **expensive** (complex initialization, database calls, etc.)
- You want to avoid **subclassing** a factory that creates objects
- You need to create objects with **similar configurations** but slight variations
- The classes to instantiate are specified at **run-time**

## 🔄 Shallow vs. Deep Cloning

### Shallow Cloning (`Structure/` implementations)
```java
// Copies object fields directly
public Prototype clone() {
    return new ConcretePrototypeA(this);
}
```

**Pros:**
- Fast cloning operation
- Simple implementation

**Cons:**  
- Shared references to mutable objects
- Changes to nested objects affect all clones

### Deep Cloning (`Example/Shape.java` approach)
```java
// Creates completely independent copies
public Shape clone() {
    return new Circle(this.color, this.x, this.y, this.radius);
}
```

**Pros:**
- Complete independence between original and clone
- Safe for objects with mutable fields

**Cons:**
- More complex implementation
- Higher memory usage

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Creational/Prototype/Java/Structure
   javac *.java
   java Main
   ```

2. Demo example with real-world scenario:
   ```bash
   cd Creational/Prototype/Java/Example
   javac *.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
=== Structure Demo: Prototype Pattern ===

1. Creating original prototypes:
ConcretePrototypeA created with data: Original Data, value: 42
ConcretePrototypeB created with name: Original Name, active: true

2. Cloning ConcretePrototypeA:
ConcretePrototypeA cloned with data: Original Data, value: 42
ConcretePrototypeA cloned with data: Original Data, value: 42
Original == Clone1: false
Clone1 == Clone2: false

Original and clones display:
ConcretePrototypeA [data=Original Data, value=42]
ConcretePrototypeA [data=Original Data, value=42]
ConcretePrototypeA [data=Original Data, value=42]

3. Modifying clone to show independence:
After modifying clone1:
Original: ConcretePrototypeA [data=Original Data, value=42]
Clone1: ConcretePrototypeA [data=Modified Data, value=99]
Clone2: ConcretePrototypeA [data=Original Data, value=42]

4. Using Client class:
Current prototype: ConcretePrototypeB [name=Original Name, active=true]
ConcretePrototypeB cloned with name: Original Name, active: true
Cloned via Client: ConcretePrototypeB [name=Original Name, active=true]
Original == Clone: false

Changed client prototype:
Current prototype: ConcretePrototypeA [data=Original Data, value=42]
ConcretePrototypeA cloned with data: Original Data, value: 42
New clone: ConcretePrototypeA [data=Original Data, value=42]

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)
```
=== Prototype Design Pattern Demo ===

1. Creating original shape prototypes:
Circle created: Circle[color=Red, x=10, y=20, radius=15]
Rectangle created: Rectangle[color=Blue, x=30, y=40, width=25, height=35]

2. Cloning shapes to create variations:
Cloning circle...
Cloning circle...
Cloning rectangle...
Cloning rectangle...

3. Drawing all shapes:
Original prototypes:
Drawing Circle at (10,20) with radius 15 in Red
Drawing Rectangle at (30,40) with size 25x35 in Blue

Cloned variations:
Drawing Circle at (50,60) with radius 15 in Green
Drawing Circle at (80,90) with radius 20 in Red
Drawing Rectangle at (100,110) with size 25x35 in Yellow
Drawing Rectangle at (120,130) with size 40x50 in Blue

4. Demonstrating object independence:
Original circle area: 706.86
Cloned circle area: 706.86
Modified circle area: 1256.64

Reference comparison:
Original == Clone1: false
Clone1 == Clone2: false

5. Performance comparison (cloning vs new creation):
Time for 1000 clones: 346159 nanoseconds
Time for 1000 new objects: 447840 nanoseconds
Cloning is 1.29x faster

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Identity Check**: `original == clone` returns `false`, proving they are separate instances
2. **Independence**: Modifying cloned objects doesn't affect the original or other clones
3. **Performance**: Cloning can be faster than creating new objects with complex initialization
4. **Flexibility**: Client can work with any prototype without knowing concrete types
5. **Polymorphism**: Different concrete prototypes can be cloned through the same interface

## 🔍 Best Practices

- Use **interfaces or abstract classes** to define the clone contract
- Implement **copy constructors** for clean cloning logic
- Consider **deep vs shallow cloning** based on your object structure
- Use prototype when object creation is **expensive or complex**
- Consider **serialization-based cloning** for complex deep cloning scenarios
- Be careful with **circular references** in deep cloning