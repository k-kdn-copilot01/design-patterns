# Composite Design Pattern - Python Implementation

This folder contains Python implementations of the **Composite** design pattern, demonstrating the core structure and a real-world file system example.

## 📁 Folder Structure

- `Structure/`
  - `Component.py` — Abstract base class defining the common interface
  - `Leaf.py` — Leaf component that cannot have children
  - `Composite.py` — Composite component that can contain other components
  - `Main.py` — Demo for structure-only implementations
- `Example/`
  - `FileSystemComponent.py` — Abstract base class for file system components
  - `File.py` — File component (leaf)
  - `Directory.py` — Directory component (composite)
  - `Main.py` — Demo using file system as a real-world example
- `README.md` — This documentation

## 🎯 When to Use Composite

The Composite pattern should be used when:
- You need to represent **part-whole hierarchies** of objects
- You want clients to treat **individual objects and compositions uniformly**
- You need to **recursively compose** tree structures
- You want to **add new types of components** without changing existing code

## 🏗️ Pattern Structure

### Core Components

#### 1. Component (`Structure/Component.py`)
```python
class Component(ABC):
    def __init__(self, name: str):
        self.name = name
        self.parent = None
    
    @abstractmethod
    def operation(self) -> str:
        pass
    
    @abstractmethod
    def add(self, component: 'Component') -> None:
        pass
    
    @abstractmethod
    def remove(self, component: 'Component') -> None:
        pass
```

**Purpose:** Defines the common interface for all objects in the composition.

#### 2. Leaf (`Structure/Leaf.py`)
```python
class Leaf(Component):
    def operation(self) -> str:
        return f"Leaf({self.name})"
    
    def add(self, component: Component) -> None:
        raise NotImplementedError("Cannot add components to a leaf")
```

**Purpose:** Represents leaf objects that cannot have children.

#### 3. Composite (`Structure/Composite.py`)
```python
class Composite(Component):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[Component] = []
    
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite({self.name})[{', '.join(results)}]"
```

**Purpose:** Represents complex objects that can contain other components.

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Structural/Composite/Python/Structure
   python Main.py
   ```

2. Demo example with file system:
   ```bash
   cd Structural/Composite/Python/Example
   python Main.py
   ```

## 📊 Expected Output (Structure/Main)

```
=== Structure Demo: Composite Pattern ===

1. Simple Leaf Components:
RESULT: Leaf(Leaf1)
RESULT: Leaf(Leaf2)

2. Complex Composite Components:
RESULT: Composite(Tree)[Composite(Branch1)[Leaf(Leaf1), Leaf(Leaf2)], Composite(Branch2)[Leaf(Leaf3)]]

3. Dynamic Component Addition:
RESULT: Composite(Tree)[Composite(Branch1)[Leaf(Leaf1), Leaf(Leaf2)], Composite(Branch2)[Leaf(Leaf3)], Leaf(Leaf4)]

4. Tree Structure Analysis:
Tree is composite: True
Tree children count: 3
Branch1 children count: 2
Branch2 children count: 1

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)

```
=== Composite Pattern Demo: File System ===

1. Building file system structure...
File system structure created successfully!

2. Displaying file system structure:
File System Structure:
==================================================
📁 Root/ (3097344 bytes)
  📄 README.txt (1024 bytes)
  📄 config.json (512 bytes)
  📄 script.py (2048 bytes)
  📁 Documents/ (15616 bytes)
    📄 report.pdf (15360 bytes)
    📄 notes.txt (256 bytes)
  📁 Images/ (3072000 bytes)
    📄 photo1.jpg (2048000 bytes)
    📄 photo2.png (1024000 bytes)
  📁 Projects/ (6144 bytes)
    📄 main.py (4096 bytes)
    📄 utils.py (2048 bytes)
==================================================

3. Calculating sizes:
Total size of 'Root': 3097344 bytes
Total size of 'Documents': 15616 bytes
Total size of 'Images': 3072000 bytes
Total size of 'Projects': 6144 bytes

4. Dynamic operations:
Added new_document.docx to Documents directory
Total size of 'Documents': 23808 bytes

Removed photo2.png from Images directory
Total size of 'Images': 2048000 bytes

Found file: main.py (4096 bytes)

5. Final file system structure:
File System Structure:
==================================================
📁 Root/ (2081536 bytes)
  📄 README.txt (1024 bytes)
  📄 config.json (512 bytes)
  📄 script.py (2048 bytes)
  📁 Documents/ (23808 bytes)
    📄 report.pdf (15360 bytes)
    📄 notes.txt (256 bytes)
    📄 new_document.docx (8192 bytes)
  📁 Images/ (2048000 bytes)
    📄 photo1.jpg (2048000 bytes)
  📁 Projects/ (6144 bytes)
    📄 main.py (4096 bytes)
    📄 utils.py (2048 bytes)
==================================================

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Uniform Interface**: Both `Leaf` and `Composite` implement the same `Component` interface
2. **Recursive Composition**: Composites can contain other composites, creating tree structures
3. **Transparent Treatment**: Clients treat individual objects and compositions uniformly
4. **Dynamic Structure**: Components can be added/removed at runtime
5. **Size Calculation**: The file system example shows how composite operations aggregate results

## 🔍 Real-World Applications

- **File Systems**: Files and directories (as demonstrated in the example)
- **GUI Components**: Windows, panels, buttons, and other UI elements
- **Organization Charts**: Employees, departments, and divisions
- **Mathematical Expressions**: Numbers, variables, and operations
- **Menu Systems**: Menu items and submenus

## 🏆 Benefits

- **Simplifies Client Code**: Clients don't need to distinguish between leaf and composite objects
- **Easy to Add New Types**: New component types can be added without changing existing code
- **Flexible Structure**: Tree structures can be built dynamically
- **Consistent Interface**: All components share the same interface

## ⚠️ Considerations

- **Type Safety**: Leaf operations (like `add`) may throw exceptions when called inappropriately
- **Performance**: Large tree structures may impact performance due to recursive operations
- **Memory Usage**: Composite objects maintain references to all their children
- **Complexity**: The pattern can make the design more general and harder to understand
