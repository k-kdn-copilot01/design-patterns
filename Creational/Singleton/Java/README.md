# Singleton Design Pattern - Java Implementation

This folder contains Java implementations of the **Singleton** design pattern, demonstrating different approaches and a real-world example.

## 📁 Folder Structure

- `Structure/`
  - `LazySingleton.java` — Lazy initialization (not thread-safe)
  - `EagerSingleton.java` — Eager initialization (thread-safe)
  - `Main.java` — Demo for structure-only implementations
- `Example/`
  - `DatabaseConnection.java` — Real-world example using synchronized method
  - `Main.java` — Demo using structure classes with an example
- `README.md` — This documentation

## 🎯 When to Use Singleton

The Singleton pattern should be used when:
- You need exactly **one instance** of a class throughout the application
- You want to control access to a shared resource (e.g., database connection, file system, logging)
- You need a global point of access to the instance
- The cost of creating the instance is high

## ⚖️ Lazy vs. Eager Initialization

### Lazy Singleton (`Structure/LazySingleton.java`)
```java
// Instance created only when first needed
if (instance == null) {
    instance = new LazySingleton();
}
```

**Pros:**
- Memory efficient - instance created only when needed
- Faster application startup

**Cons:**
- **Not thread-safe** - multiple threads can create multiple instances
- Slightly slower first access due to null check

### Eager Singleton (`Structure/EagerSingleton.java`)
```java
// Instance created at class loading time
private static final EagerSingleton instance = new EagerSingleton();
```

**Pros:**
- **Thread-safe** - JVM handles class loading synchronization
- Fast access - no null checks needed
- Simple implementation

**Cons:**
- Memory usage - instance created even if never used
- Slower application startup if constructor is heavy

### Thread-Safe Lazy Singleton (`Example/DatabaseConnection.java`)
```java
// Synchronized method ensures thread safety
public static synchronized DatabaseConnection getInstance() {
    if (instance == null) {
        instance = new DatabaseConnection();
    }
    return instance;
}
```

**Pros:**
- Thread-safe lazy initialization
- Memory efficient

**Cons:**
- Slower access due to synchronization overhead
- Can become a bottleneck in high-concurrency scenarios

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Creational/Singleton/Java/Structure
   javac *.java
   java Main
   ```

2. Demo example with structure classes:
   ```bash
   cd Creational/Singleton/Java/Example
   javac ../Structure/*.java *.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
=== Structure Demo: Singleton Implementations ===

1. Lazy Singleton:
LazySingleton instance created
lazy1 == lazy2: true
LazySingleton is doing something...

2. Eager Singleton:
EagerSingleton instance created
EagerSingleton instance created
EagerSingleton is doing something...

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)
```
=== Singleton Design Pattern Demo ===

1. Testing Lazy Singleton:
LazySingleton instance created
lazy1 == lazy2: true
LazySingleton is doing something...

2. Testing Eager Singleton:
eager1 == eager2: true
EagerSingleton is doing something...

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Identity Check**: `instance1 == instance2` returns `true`, proving only one instance exists
2. **Eager vs Lazy**: Notice that `EagerSingleton` is created immediately, while `LazySingleton` is created on first access
3. **Shared State**: All references point to the same instance, so state changes are shared
4. **Thread Safety**: Choose the right implementation based on your threading requirements

## 🔍 Best Practices

- Use **Eager Singleton** for lightweight objects that are always needed
- Use **Thread-Safe Lazy Singleton** for heavy objects that might not be needed
- Consider using **enum-based Singleton** for ultimate simplicity and thread safety
- Be careful with **Lazy Singleton** in multi-threaded environments