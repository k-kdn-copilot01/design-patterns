# Iterator Design Pattern - Python Implementation

This folder contains Python implementations of the **Iterator** design pattern, demonstrating the core structure and a real-world library management system example.

## 📁 Folder Structure

- `Structure/`
  - `Iterator.py` — Abstract iterator interface
  - `IterableCollection.py` — Abstract collection interface
  - `ConcreteIterator.py` — Concrete iterator implementation
  - `ConcreteCollection.py` — Concrete collection implementation
  - `Main.py` — Demo for structure-only implementations
- `Example/`
  - `Book.py` — Book entity for library system
  - `LibraryCatalog.py` — Library catalog collection
  - `BookIterator.py` — Various iterator implementations (all books, available books, genre-specific)
  - `Main.py` — Demo using library management system
- `README.md` — This documentation

## 🎯 When to Use Iterator

The Iterator pattern should be used when:
- You need to **traverse a collection** without exposing its internal structure
- You want to provide **multiple ways** to iterate over the same collection
- You need to **support multiple simultaneous iterations** over the same collection
- You want to **decouple traversal algorithms** from the collection structure
- You need to **iterate over different types of collections** using a uniform interface

## 🏗️ Pattern Structure

### Core Components

#### 1. Iterator Interface (`Structure/Iterator.py`)
```python
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        """Returns True if iteration has more elements"""
        pass
    
    @abstractmethod
    def next(self) -> Any:
        """Returns the next element in the iteration"""
        pass
    
    @abstractmethod
    def reset(self) -> None:
        """Resets the iterator to the beginning"""
        pass
```

#### 2. IterableCollection Interface (`Structure/IterableCollection.py`)
```python
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Creates and returns an iterator for this collection"""
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """Returns the size of the collection"""
        pass
    
    @abstractmethod
    def get_item(self, index: int) -> Any:
        """Returns the item at the specified index"""
        pass
```

#### 3. Concrete Iterator (`Structure/ConcreteIterator.py`)
```python
class ConcreteIterator(Iterator):
    def __init__(self, collection: IterableCollection):
        self._collection = collection
        self._current_index = 0
    
    def has_next(self) -> bool:
        return self._current_index < self._collection.get_size()
    
    def next(self) -> Any:
        if not self.has_next():
            raise StopIteration("No more elements to iterate")
        item = self._collection.get_item(self._current_index)
        self._current_index += 1
        return item
```

## 🚀 How to Run

### 1. Structure Demo (Basic Pattern Implementation)
```bash
cd Behavioral/Iterator/Python/Structure
python Main.py
```

### 2. Example Demo (Library Management System)
```bash
cd Behavioral/Iterator/Python/Example
python Main.py
```

## 📊 Expected Output (Structure/Main.py)

```
=== Structure Demo: Iterator Design Pattern ===

Collection created with 5 items: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

1. Forward iteration:
   Iterating through the collection:
   - Apple
   - Banana
   - Cherry
   - Date
   - Elderberry

2. Reset and iterate again:
   Iterator reset to beginning
   Iterating through the collection again:
   - Apple
   - Banana
   - Cherry
   - Date
   - Elderberry

3. Iterator state demonstration:
   Initial index: 0
   After getting 'Apple': index = 1
   After getting 'Banana': index = 2
   After getting 'Cherry': index = 3
   Has more items: True

4. Error handling demonstration:
   All items consumed
   Has more items: False
   Caught StopIteration: No more elements to iterate

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main.py)

```
=== Iterator Design Pattern Demo: Library Management System ===

Library created with 10 books
Available books: 7
Borrowed books: 3

1. Iterating through ALL books in the library:
   ============================================================
    1. Clean Code by Robert C. Martin (2008) - Borrowed
    2. Design Patterns by Gang of Four (1994) - Available
    3. Effective Java by Joshua Bloch (2017) - Available
    4. The Great Gatsby by F. Scott Fitzgerald (1925) - Borrowed
    5. To Kill a Mockingbird by Harper Lee (1960) - Available
    6. Pride and Prejudice by Jane Austen (1813) - Available
    7. The Catcher in the Rye by J.D. Salinger (1951) - Available
    8. The Alchemist by Paulo Coelho (1988) - Available
    9. The Da Vinci Code by Dan Brown (2003) - Borrowed
   10. Gone Girl by Gillian Flynn (2012) - Available

2. Iterating through AVAILABLE books only:
   ============================================================
    1. Design Patterns by Gang of Four (1994) - Available
    2. Effective Java by Joshua Bloch (2017) - Available
    3. To Kill a Mockingbird by Harper Lee (1960) - Available
    4. Pride and Prejudice by Jane Austen (1813) - Available
    5. The Catcher in the Rye by J.D. Salinger (1951) - Available
    6. The Alchemist by Paulo Coelho (1988) - Available
    7. Gone Girl by Gillian Flynn (2012) - Available

3. Iterating through FICTION books:
   ============================================================
    1. The Great Gatsby by F. Scott Fitzgerald (1925) - Borrowed
    2. To Kill a Mockingbird by Harper Lee (1960) - Available
    3. Pride and Prejudice by Jane Austen (1813) - Available
    4. The Catcher in the Rye by J.D. Salinger (1951) - Available
    5. The Alchemist by Paulo Coelho (1988) - Available

4. Iterating through PROGRAMMING books:
   ============================================================
    1. Clean Code by Robert C. Martin (2008) - Borrowed
    2. Design Patterns by Gang of Four (1994) - Available
    3. Effective Java by Joshua Bloch (2017) - Available

5. Demonstrating iterator reset functionality:
   ============================================================
   First iteration (first 3 books):
   - Clean Code
   - Design Patterns
   - Effective Java
   Current position: 3
   Resetting iterator...
   Position after reset: 0
   Second iteration (first 3 books again):
   - Clean Code
   - Design Patterns
   - Effective Java

6. Demonstrating dynamic collection changes:
   ============================================================
   Added new book: Python Crash Course
   Updated library contents:
   - Clean Code
   - Design Patterns
   - Effective Java
   - The Great Gatsby
   - To Kill a Mockingbird
   - Pride and Prejudice
   - The Catcher in the Rye
   - The Alchemist
   - The Da Vinci Code
   - Gone Girl
   - Python Crash Course by Eric Matthes (2019) - Available (NEW!)

7. Demonstrating error handling:
   ============================================================
   Has books in 'NonExistentGenre': False
   Caught StopIteration: No more NonExistentGenre books to iterate

=== Library Management Demo Complete ===

=== Iterator Pattern Benefits Demonstration ===

Benefits of Iterator Pattern:
1. UNIFORM INTERFACE: Same interface for different iteration types
   - All books iterator
   - Available books iterator
   - Genre-specific iterator

2. ENCAPSULATION: Internal collection structure is hidden
   - Client code doesn't need to know how books are stored
   - Can change internal storage without affecting client code

3. MULTIPLE ITERATIONS: Can have multiple iterators simultaneously
   - Each iterator maintains its own state
   - Independent iteration progress

4. SIMULTANEOUS ITERATIONS:
   Iterator 1 (All books) - Iterator 2 (Fiction books)
   --------------------------------------------------
    1. Clean Code                 | The Great Gatsby
    2. Design Patterns            | To Kill a Mockingbird
    3. Effective Java             | Pride and Prejudice

=== Benefits Demonstration Complete ===
```

## 🎓 Key Learning Points

### 1. **Encapsulation**
- The Iterator pattern hides the internal structure of the collection
- Client code doesn't need to know how items are stored (list, tree, etc.)
- Changes to internal storage don't affect client code

### 2. **Multiple Iteration Types**
- Same collection can be iterated in different ways
- Examples: all items, filtered items, sorted items, reverse order
- Each iterator type encapsulates its own traversal logic

### 3. **State Management**
- Each iterator maintains its own position/state
- Multiple iterators can work simultaneously on the same collection
- Iterator state is independent of the collection state

### 4. **Uniform Interface**
- All iterators implement the same interface (`has_next()`, `next()`, `reset()`)
- Client code can work with any iterator without knowing its specific type
- Enables polymorphic iteration over different collection types

### 5. **Error Handling**
- Proper exception handling for boundary conditions
- `StopIteration` exception when no more elements are available
- Graceful handling of empty collections

## 🔍 Real-World Applications

### 1. **Database Result Sets**
```python
# Iterate through database query results
for row in database_cursor:
    process_row(row)
```

### 2. **File System Traversal**
```python
# Iterate through files in a directory
for file in directory_iterator:
    process_file(file)
```

### 3. **Tree Traversal**
```python
# Different ways to traverse a tree
for node in preorder_iterator(tree):
    process_node(node)

for node in inorder_iterator(tree):
    process_node(node)
```

### 4. **Stream Processing**
```python
# Process data streams
for chunk in stream_iterator:
    process_chunk(chunk)
```

## 🏆 Benefits

### ✅ **Advantages**
- **Encapsulation**: Hides collection internals
- **Flexibility**: Multiple iteration strategies
- **Reusability**: Same iterator can be used multiple times
- **Polymorphism**: Uniform interface for different collections
- **Concurrent Access**: Multiple simultaneous iterations
- **Lazy Evaluation**: Items can be computed on-demand

### ⚠️ **Considerations**
- **Memory Overhead**: Each iterator maintains state
- **Complexity**: Additional abstraction layer
- **Performance**: Slight overhead compared to direct access
- **Overkill**: May be unnecessary for simple collections

## 🔧 Best Practices

1. **Use Abstract Interfaces**: Define clear contracts for iterators and collections
2. **Handle Edge Cases**: Properly handle empty collections and boundary conditions
3. **Immutable Iterators**: Consider making iterators immutable when possible
4. **Resource Management**: Clean up resources when iteration is complete
5. **Thread Safety**: Consider thread safety if collections are accessed concurrently
6. **Performance**: Use lazy evaluation for large collections
7. **Error Handling**: Provide meaningful error messages and handle exceptions gracefully

## 🆚 Iterator vs. Built-in Python Iteration

### Python's Built-in Iteration
```python
# Python's built-in iteration
for item in my_list:
    print(item)
```

### Iterator Pattern
```python
# Iterator pattern
iterator = collection.create_iterator()
while iterator.has_next():
    item = iterator.next()
    print(item)
```

**When to use Iterator Pattern over built-in iteration:**
- Need multiple simultaneous iterations
- Require custom traversal logic
- Want to hide collection implementation details
- Need to support different iteration strategies
- Working with complex data structures

## 🔗 Related Patterns

- **Composite**: Iterator is often used to traverse composite structures
- **Visitor**: Iterator can work with Visitor to perform operations on each element
- **Factory Method**: Used to create appropriate iterator instances
- **Memento**: Can be used to save and restore iterator state
