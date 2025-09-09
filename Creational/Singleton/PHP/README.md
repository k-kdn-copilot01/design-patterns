# Singleton Design Pattern - PHP Implementation

This folder contains PHP implementations of the **Singleton** design pattern, demonstrating different approaches and a real-world example.

## 📁 Files Overview

- **`LazySingleton.php`** - Lazy initialization (single-threaded)
- **`EagerSingleton.php`** - Eager initialization (with simulated early loading)
- **`DatabaseConnection.php`** - Real-world example for database connections
- **`main.php`** - Demo script to run all examples
- **`README.md`** - This documentation

## 🎯 When to Use Singleton

The Singleton pattern should be used when:
- You need exactly **one instance** of a class throughout the application
- You want to control access to a shared resource (e.g., database connection, file system, logging)
- You need a global point of access to the instance
- The cost of creating the instance is high

## ⚖️ Lazy vs. Eager Initialization

### Lazy Singleton (`LazySingleton.php`)
```php
// Instance created only when first needed
if (self::$instance === null) {
    self::$instance = new self();
}
```

**Pros:**
- Memory efficient - instance created only when needed
- Faster application startup

**Cons:**
- Slightly slower first access due to null check
- In PHP web apps, thread safety is less of a concern due to single-threaded nature per request

### Eager Singleton (`EagerSingleton.php`)
```php
// Instance created at class loading time (simulated)
EagerSingleton::getInstance(); // Called at end of class file
```

**Pros:**
- Fast access - instance ready when class is loaded
- Simple implementation
- Consistent behavior

**Cons:**
- Memory usage - instance created even if never used
- Slightly slower application startup if constructor is heavy

### Database Connection Singleton (`DatabaseConnection.php`)
```php
// Standard lazy initialization - suitable for PHP
public static function getInstance() {
    if (self::$instance === null) {
        self::$instance = new self();
    }
    return self::$instance;
}
```

**Pros:**
- Memory efficient lazy initialization
- Perfect for managing expensive resources like database connections
- Prevents multiple connections in the same request

**Cons:**
- Slight overhead on first access

## 🚀 How to Run

1. **Make sure PHP is installed:**
   ```bash
   php --version
   ```

2. **Navigate to the PHP directory:**
   ```bash
   cd Creational/Singleton/PHP/
   ```

3. **Run the demo:**
   ```bash
   php main.php
   ```

## 📊 Expected Output

```
=== Singleton Design Pattern Demo ===

EagerSingleton instance created
1. Testing Lazy Singleton:
LazySingleton instance created
lazy1 === lazy2: true
LazySingleton is doing something...

2. Testing Eager Singleton:
eager1 === eager2: true
EagerSingleton is doing something...

3. Testing Database Connection Singleton:
DatabaseConnection instance created
db1 === db2: true
Connection String: mysql:host=localhost;dbname=mydb;charset=utf8
Connecting to database: mysql:host=localhost;dbname=mydb;charset=utf8
Database connection established
Executing query: SELECT * FROM users
Query executed successfully
Executing query: SELECT * FROM products
Query executed successfully
Disconnecting from database
Database connection closed
Error: No database connection. Please connect first.

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Identity Check**: `$instance1 === $instance2` returns `true`, proving only one instance exists
2. **Eager vs Lazy**: Notice that `EagerSingleton` is created immediately when the class is loaded, while `LazySingleton` is created on first access
3. **Shared State**: All references point to the same instance, so state changes are shared
4. **PHP-Specific**: Thread safety is less of a concern in PHP web applications due to their single-threaded nature per request

## 🔍 PHP-Specific Best Practices

- Use **private constructor** to prevent external instantiation
- Implement **`__clone()`** and **`__wakeup()`** as private to prevent cloning and unserialization
- Use **`===`** for identity comparison instead of `==`
- Use **Database Connection Singleton** for PDO connections, Redis clients, or other expensive resources
- Consider using **dependency injection** for better testability in larger applications
- For **session management**, configuration objects, or **logging**, Singleton can be very useful

## 💡 Real-World Use Cases in PHP

- **Database connections** (PDO instances)
- **Configuration managers** (loading config files once)
- **Logging systems** (single log file handler)
- **Cache managers** (Redis/Memcached connections)
- **Session handlers** (custom session management)

## ⚠️ Considerations

- **Testing**: Singletons can make unit testing difficult. Consider using dependency injection for better testability
- **Global State**: Be careful with global state management
- **Memory**: In long-running PHP applications (like ReactPHP or Swoole), be mindful of memory usage