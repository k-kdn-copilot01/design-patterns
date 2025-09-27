# Memento Pattern

The **Memento Pattern** is a behavioral design pattern that provides the ability to restore an object to its previous state without violating encapsulation. It allows you to save and restore the state of an object at any point in time, which is particularly useful for implementing undo/redo functionality, checkpoints, and state snapshots.

## 🎯 Intent

- Save and restore the state of an object without exposing its internal structure
- Provide a way to implement undo/redo functionality
- Enable checkpoint and rollback mechanisms
- Maintain encapsulation while allowing state preservation

## 🏗️ Structure

The Memento pattern consists of three main components:

### 1. **Originator**
- The object whose state needs to be saved and restored
- Creates mementos containing snapshots of its current state
- Uses mementos to restore its state to a previous state

### 2. **Memento**
- Stores the internal state of the Originator
- Provides methods to retrieve the saved state
- Should not expose the Originator's internal structure

### 3. **Caretaker**
- Manages and stores mementos
- Never operates on or examines the contents of a memento
- Can save, retrieve, and manage the history of mementos

## 📁 Project Structure

```
Behavioral/Memento/Python/
├── Structure/           # Core pattern implementation
│   ├── memento.py      # Memento, Originator, Caretaker classes
│   └── main.py         # Structure demo
├── Example/            # Real-world example
│   ├── text_editor.py  # Text editor with undo/redo
│   └── main.py         # Example demo
└── README.md           # This file
```

## 🚀 How to Run

### Structure Demo (Basic Pattern)

Navigate to the Structure directory and run the basic pattern demonstration:

```bash
cd Behavioral/Memento/Python/Structure
python main.py
```

**Expected Output:**
```
============================================================
MEMENTO PATTERN - STRUCTURE DEMO
============================================================

1. Creating Originator with initial state...
Current State:
  name: John Doe
  age: 30
  position: Developer
  salary: 75000

2. Creating Caretaker to manage state history...

3. Saving initial state...
✓ Initial state saved
History (1 snapshots):
  [0] {'name': 'John Doe', 'age': 30, 'position': 'Developer', 'salary': 75000} <-- Current

4. Modifying state (promotion)...
Current State:
  name: John Doe
  age: 31
  position: Senior Developer
  salary: 90000

5. Saving modified state...
✓ Modified state saved
History (2 snapshots):
  [0] {'name': 'John Doe', 'age': 30, 'position': 'Developer', 'salary': 75000}
  [1] {'name': 'John Doe', 'age': 31, 'position': 'Senior Developer', 'salary': 90000} <-- Current

... (continues with more state changes and restorations)

============================================================
MEMENTO PATTERN DEMO COMPLETED
============================================================
```

### Example Demo (Text Editor)

Navigate to the Example directory and run the real-world example:

```bash
cd Behavioral/Memento/Python/Example
python main.py
```

**Expected Output:**
```
======================================================================
MEMENTO PATTERN - REAL-WORLD EXAMPLE: TEXT EDITOR
======================================================================

1. Initializing text editor with undo/redo functionality...
✓ Initial empty state saved
Content: ''
Cursor:  ^ (position 0)

2. Typing a document...
Typing: 'Hello'
  Added 'H' -> H
  Added 'e' -> He
  Added 'l' -> Hel
  Added 'l' -> Hell
  Added 'o' -> Hello

Typing: ' World!'
  Added ' ' -> Hello 
  Added 'W' -> Hello W
  Added 'o' -> Hello Wo
  Added 'r' -> Hello Wor
  Added 'l' -> Hello Worl
  Added 'd' -> Hello World
  Added '!' -> Hello World!

... (continues with editing session, undo/redo operations)

======================================================================
TEXT EDITOR DEMO COMPLETED
======================================================================
```

## 🔍 Key Features Demonstrated

### Structure Demo
- ✅ **State Management**: Save and restore object state
- ✅ **History Navigation**: Move forward/backward through state history
- ✅ **Encapsulation**: State is preserved without exposing internal structure
- ✅ **Multiple Snapshots**: Save multiple states and restore to any of them

### Example Demo
- ✅ **Undo/Redo Functionality**: Complete text editor with undo/redo
- ✅ **Character-by-Character Tracking**: Save state after each keystroke
- ✅ **Cursor Position Management**: Preserve cursor position in snapshots
- ✅ **History Limiting**: Efficient memory usage with limited history
- ✅ **Error Recovery**: Recover from accidental data loss
- ✅ **Timestamp Tracking**: Track when each state was saved

## 💡 Use Cases

The Memento pattern is particularly useful for:

1. **Text Editors**: Undo/redo functionality
2. **Games**: Save/load game states, checkpoints
3. **Database Systems**: Transaction rollback
4. **Configuration Management**: Restore previous configurations
5. **Drawing Applications**: Undo/redo drawing operations
6. **Web Applications**: Browser back/forward navigation
7. **Version Control**: Restore to previous versions

## ⚡ Benefits

- **Encapsulation**: Doesn't expose the Originator's internal structure
- **Flexibility**: Can save and restore state at any point
- **Reusability**: Caretaker can manage multiple types of mementos
- **Memory Efficiency**: Can limit history size to prevent memory issues
- **Error Recovery**: Provides a way to recover from mistakes

## ⚠️ Considerations

- **Memory Usage**: Storing many mementos can consume significant memory
- **Performance**: Creating mementos for large objects can be expensive
- **State Complexity**: Complex objects may require deep copying
- **History Management**: Need to decide when to save states and how many to keep

## 🔧 Implementation Notes

### Structure Implementation
- Uses dictionaries to store state for simplicity
- Provides methods for state manipulation and retrieval
- Implements history navigation with index tracking
- Includes comprehensive state display methods

### Example Implementation
- Text editor with character-by-character state saving
- Cursor position tracking in mementos
- Timestamp information for each saved state
- Memory-efficient history management with size limits
- Error recovery demonstration

## 📚 Related Patterns

- **Command Pattern**: Often used together for implementing undo/redo
- **State Pattern**: Can be combined for complex state management
- **Prototype Pattern**: Alternative approach for object state cloning

## 🎓 Learning Outcomes

After studying this implementation, you should understand:

1. How to implement the Memento pattern in Python
2. When and why to use the Memento pattern
3. How to manage state history efficiently
4. How to implement undo/redo functionality
5. How to balance memory usage with functionality
6. How to maintain encapsulation while preserving state

---

*This implementation provides both a clear structural example and a practical real-world application, making it easy to understand and apply the Memento pattern in your own projects.*
