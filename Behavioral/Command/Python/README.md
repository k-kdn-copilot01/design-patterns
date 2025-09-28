# Command Design Pattern - Python Implementation

This folder contains Python implementations of the **Command** design pattern, demonstrating the core structure and a real-world text editor example with undo/redo functionality.

## 📁 Folder Structure

- `Structure/`
  - `Command.py` — Abstract command interface
  - `Receiver.py` — Object that performs the actual work
  - `ConcreteCommand.py` — Concrete implementation of commands
  - `Invoker.py` — Object that invokes commands and manages history
  - `Main.py` — Demo for structure-only implementations
- `Example/`
  - `TextEditor.py` — Real-world receiver (text editor)
  - `TextCommand.py` — Concrete text editor commands
  - `TextEditorInvoker.py` — Invoker with undo/redo functionality
  - `Main.py` — Demo using text editor example
- `README.md` — This documentation

## 🎯 When to Use Command Pattern

The Command pattern should be used when:
- You need to **parameterize objects** with operations
- You want to **queue, log, or undo** operations
- You need to **support macro operations** (composite commands)
- You want to **decouple** the object that invokes the operation from the object that performs it
- You need to **support callbacks** or **function objects**

## 🏗️ Pattern Structure

### Core Components

1. **Command Interface** (`Command.py`)
   - Declares the interface for executing operations
   - Usually includes `execute()` and `undo()` methods

2. **Concrete Command** (`ConcreteCommand.py`)
   - Implements the Command interface
   - Stores parameters for the operation
   - Delegates to the receiver

3. **Receiver** (`Receiver.py`)
   - Contains the actual business logic
   - Knows how to perform operations

4. **Invoker** (`Invoker.py`)
   - Asks the command to carry out the request
   - Can store commands for undo/redo functionality

## ⚖️ Structure vs Example Implementation

### Structure Implementation (`Structure/`)
```python
# Basic command pattern demonstration
command = ConcreteCommand(receiver, "message")
invoker.set_command(command)
invoker.execute_commands()
```

**Features:**
- Basic command execution
- Simple undo functionality
- Command history management
- Clear separation of concerns

### Example Implementation (`Example/`)
```python
# Real-world text editor with undo/redo
insert_command = InsertTextCommand(editor, "Hello")
invoker.execute_command(insert_command)
invoker.undo()  # Undo the insertion
invoker.redo()  # Redo the insertion
```

**Features:**
- Text editor with insert/delete operations
- Full undo/redo functionality
- Cursor position management
- Real-world business logic

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Behavioral/Command/Python/Structure
   python Main.py
   ```

2. Demo example with text editor:
   ```bash
   cd Behavioral/Command/Python/Example
   python Main.py
   ```

## 📊 Expected Output (Structure/Main)

```
=== Structure Demo: Command Pattern ===

1. Setting up commands:
Commands added to invoker

2. Executing all commands:
BusinessLogic: Executing action - Save data to database
BusinessLogic: Executing action - Send email notification
BusinessLogic: Executing action - Generate report
History size: 3

3. Undoing last command:
BusinessLogic: Undoing action - Generate report
History size after undo: 2

4. Undoing all remaining commands:
BusinessLogic: Undoing action - Send email notification
BusinessLogic: Undoing action - Save data to database
History size after undo all: 0

5. Testing individual command execution:
BusinessLogic: Executing action - Single operation
BusinessLogic: Undoing action - Single operation

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)

```
=== Command Pattern Demo: Text Editor with Undo/Redo ===

Initial state:
Content: ''
Cursor position: 0

1. Inserting text 'Hello ' at the beginning:
Inserted 'Hello ' at position 0
Content: 'Hello '
Cursor position: 6
Command executed and added to history

2. Inserting text 'World!' at the end:
Inserted 'World!' at position 6
Content: 'Hello World!'
Cursor position: 12
Command executed and added to history

3. Inserting text 'Beautiful ' in the middle:
Inserted 'Beautiful ' at position 6
Content: 'Hello Beautiful World!'
Cursor position: 16
Command executed and added to history

Current state - History size: 3
Content: 'Hello Beautiful World!'

4. Undoing last command (removing 'Beautiful '):
Deleted 'Beautiful ' from position 6
Content: 'Hello World!'
Cursor position: 6
Last command undone

5. Undoing another command (removing 'World!'):
Deleted 'World!' from position 6
Content: 'Hello '
Cursor position: 6
Last command undone

6. Redoing last undone command (adding 'World!' back):
Inserted 'World!' at position 6
Content: 'Hello World!'
Cursor position: 12
Command redone

7. Deleting text 'Hello ' from the beginning:
Deleted 'Hello ' from position 0
Content: 'World!'
Cursor position: 0
Command executed and added to history

8. Undoing the delete operation:
Inserted 'Hello ' at position 0
Content: 'Hello World!'
Cursor position: 6
Last command undone

9. Testing multiple undos:
Undoing all remaining commands...
Deleted 'World!' from position 6
Content: 'Hello '
Cursor position: 6
Last command undone
Deleted 'Hello ' from position 0
Content: ''
Cursor position: 0
Last command undone
Final content: ''
History size: 0
Redo stack size: 2

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Decoupling**: The invoker doesn't need to know about the receiver or the specific operation
2. **Undo/Redo**: Commands can store state to support undo operations
3. **Macro Commands**: Multiple commands can be grouped and executed together
4. **Logging**: All operations can be logged since they go through commands
5. **Queuing**: Commands can be queued for later execution

## 🔍 Best Practices

- **Keep commands simple**: Each command should do one thing well
- **Store state for undo**: Commands should store enough information to undo themselves
- **Use composition**: Create macro commands by composing multiple simple commands
- **Consider memory**: Command history can grow large; implement limits if needed
- **Thread safety**: Consider thread safety if commands are executed from multiple threads

## 🌟 Real-World Applications

- **Text Editors**: Undo/redo functionality
- **GUI Applications**: Button actions, menu commands
- **Database Operations**: Transaction rollback
- **Game Development**: Replay systems, cheat codes
- **Remote Procedure Calls**: Network command execution
- **Macro Recording**: Recording and replaying user actions
