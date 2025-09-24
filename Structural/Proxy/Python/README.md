# Proxy Design Pattern - Python Implementation

This folder contains Python implementations of the **Proxy** design pattern, demonstrating the structural pattern that provides a placeholder or surrogate for another object to control access to it.

## 📁 Folder Structure

- `Structure/`
  - `Subject.py` — Abstract interface defining common operations
  - `RealSubject.py` — The actual object that performs the real work
  - `Proxy.py` — Proxy object that controls access to RealSubject
  - `Main.py` — Demo for structure-only implementations
- `Example/`
  - `FileAccess.py` — Real-world example with file access control, caching, and logging
  - `Main.py` — Demo using practical file access scenario
- `README.md` — This documentation

## 🎯 When to Use Proxy Pattern

The Proxy pattern should be used when:

- You need to **control access** to an object (access control, lazy loading)
- You want to add **additional functionality** without changing the original object
- You need to **cache expensive operations** or results
- You want to **log or monitor** access to an object
- You need to **defer object creation** until it's actually needed (lazy initialization)
- You want to provide a **local representation** of a remote object

## 🏗️ Pattern Structure

### Core Components

1. **Subject** (Abstract Interface)
   - Defines the common interface for both RealSubject and Proxy
   - Ensures Proxy can be used as a substitute for RealSubject

2. **RealSubject** (Real Object)
   - The actual object that performs the real work
   - Contains the core business logic

3. **Proxy** (Surrogate Object)
   - Maintains a reference to RealSubject
   - Controls access to RealSubject
   - Can add additional functionality (caching, logging, access control)

### Class Diagram
```
Subject (interface)
    ↑
    │
    ├── RealSubject
    └── Proxy ──→ RealSubject
```

## 🚀 How to Run

### 1. Structure Demo (Basic Implementation)

```bash
cd Structural/Proxy/Python/Structure
python Main.py
```

**Expected Output:**
```
=== Proxy Pattern Structure Demo ===

1. Direct access to RealSubject:
----------------------------------------
RealSubject: Handling request...
Result: RealSubject: Request completed successfully

2. Access through Proxy:
----------------------------------------
Proxy: Intercepting request...
Proxy: Creating RealSubject instance...
Proxy: Delegating request to RealSubject...
RealSubject: Handling request...
Proxy: Request completed
Result: Proxy: RealSubject: Request completed successfully

3. Multiple requests through Proxy (lazy initialization):
----------------------------------------
First request:
Proxy: Intercepting request...
Proxy: Creating RealSubject instance...
Proxy: Delegating request to RealSubject...
RealSubject: Handling request...
Proxy: Request completed
Result: Proxy: RealSubject: Request completed successfully

Second request (RealSubject already exists):
Proxy: Intercepting request...
Proxy: Delegating request to RealSubject...
RealSubject: Handling request...
Proxy: Request completed
Result: Proxy: RealSubject: Request completed successfully

4. Interface compatibility demonstration:
----------------------------------------
Subject 1 (RealSubject):
RealSubject: Handling request...
Result: RealSubject: Request completed successfully

Subject 2 (Proxy):
Proxy: Intercepting request...
Proxy: Creating RealSubject instance...
Proxy: Delegating request to RealSubject...
RealSubject: Handling request...
Proxy: Request completed
Result: Proxy: RealSubject: Request completed successfully

=== Structure Demo Complete ===
```

### 2. Example Demo (Real-World Scenario)

```bash
cd Structural/Proxy/Python/Example
python Main.py
```

**Expected Output:**
```
=== Proxy Pattern Real-World Example: File Access Control ===

Created test files in: /tmp/tmpXXXXXX

1. Direct File Access (without proxy):
--------------------------------------------------
RealFileAccess: Reading file '/tmp/tmpXXXXXX/public.txt'...
RealFileAccess: Successfully read 50 characters from '/tmp/tmpXXXXXX/public.txt'
Content: This is a public file that everyone can read.

2. Guest Access through Proxy:
--------------------------------------------------
Guest reading public file:
FileAccessProxy: Intercepting read request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Delegating read request to RealFileAccess...
FileAccessProxy: Creating RealFileAccess instance...
RealFileAccess: Reading file '/tmp/tmpXXXXXX/public.txt'...
RealFileAccess: Successfully read 50 characters from '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: Cached content for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] guest: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Content: This is a public file that everyone can read.

Guest trying to write file:
FileAccessProxy: Intercepting write request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: [2024-01-01 12:00:00] guest: write '/tmp/tmpXXXXXX/public.txt' - DENIED
FileAccessProxy: Access denied - 'guest' role cannot write files
Write successful: False

3. User Access through Proxy:
--------------------------------------------------
User reading public file:
FileAccessProxy: Intercepting read request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Returning cached content for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] user: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Content: [CACHED] This is a public file that everyone can read.

User writing to file:
FileAccessProxy: Intercepting write request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Delegating write request to RealFileAccess...
RealFileAccess: Writing 25 characters to '/tmp/tmpXXXXXX/public.txt'...
RealFileAccess: Successfully wrote to '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: Cleared cache for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] user: write '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Write successful: True

4. Admin Access through Proxy:
--------------------------------------------------
Admin reading public file:
FileAccessProxy: Intercepting read request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Delegating read request to RealFileAccess...
RealFileAccess: Reading file '/tmp/tmpXXXXXX/public.txt'...
RealFileAccess: Successfully read 25 characters from '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: Cached content for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] admin: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Content: Content modified by user

Admin writing to file:
FileAccessProxy: Intercepting write request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Delegating write request to RealFileAccess...
RealFileAccess: Writing 26 characters to '/tmp/tmpXXXXXX/public.txt'...
RealFileAccess: Successfully wrote to '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: Cleared cache for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] admin: write '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Write successful: True

5. Caching Functionality:
--------------------------------------------------
First read (will be cached):
FileAccessProxy: Intercepting read request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Delegating read request to RealFileAccess...
RealFileAccess: Reading file '/tmp/tmpXXXXXX/public.txt'...
RealFileAccess: Successfully read 26 characters from '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: Cached content for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] user: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Content: Content modified by admin

Second read (from cache):
FileAccessProxy: Intercepting read request for '/tmp/tmpXXXXXX/public.txt'...
FileAccessProxy: Returning cached content for '/tmp/tmpXXXXXX/public.txt'
FileAccessProxy: [2024-01-01 12:00:00] user: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
Content: [CACHED] Content modified by admin

6. Access Logs:
--------------------------------------------------
Guest access log:
  [2024-01-01 12:00:00] guest: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
  [2024-01-01 12:00:00] guest: write '/tmp/tmpXXXXXX/public.txt' - DENIED

User access log:
  [2024-01-01 12:00:00] user: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
  [2024-01-01 12:00:00] user: write '/tmp/tmpXXXXXX/public.txt' - SUCCESS
  [2024-01-01 12:00:00] user: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
  [2024-01-01 12:00:00] user: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS

Admin access log:
  [2024-01-01 12:00:00] admin: read '/tmp/tmpXXXXXX/public.txt' - SUCCESS
  [2024-01-01 12:00:00] admin: write '/tmp/tmpXXXXXX/public.txt' - SUCCESS

7. Error Handling:
--------------------------------------------------
Trying to read non-existent file:
FileAccessProxy: Intercepting read request for 'nonexistent.txt'...
FileAccessProxy: Delegating read request to RealFileAccess...
RealFileAccess: File 'nonexistent.txt' not found
FileAccessProxy: [2024-01-01 12:00:00] user: read 'nonexistent.txt' - DENIED
Content: Error: File 'nonexistent.txt' not found

Cleaned up test files in: /tmp/tmpXXXXXX

=== Real-World Example Demo Complete ===

=== Proxy Pattern Benefits Demonstration ===

Benefits of Proxy Pattern:
1. Access Control: Different user roles have different permissions
2. Lazy Loading: RealFileAccess is created only when needed
3. Caching: Frequently accessed files are cached for performance
4. Logging: All file access attempts are logged for security
5. Error Handling: Centralized error handling and validation
6. Interface Consistency: Proxy implements the same interface as RealSubject

Real-world use cases:
- Database connection pooling
- Web service API rate limiting
- Image loading with lazy loading and caching
- Security access control systems
- Remote object access (RMI, CORBA)
```

## 🎓 Key Learning Points

### Structure Demo
1. **Lazy Initialization**: RealSubject is created only when first accessed through Proxy
2. **Interface Consistency**: Both Proxy and RealSubject implement the same Subject interface
3. **Transparent Substitution**: Client code can use Proxy and RealSubject interchangeably
4. **Additional Functionality**: Proxy can add logging, caching, or access control without changing RealSubject

### Example Demo
1. **Access Control**: Different user roles (guest, user, admin) have different permissions
2. **Caching**: File content is cached to avoid repeated expensive file operations
3. **Logging**: All access attempts are logged with timestamps for security auditing
4. **Error Handling**: Centralized error handling and validation
5. **Performance**: Lazy loading and caching improve performance

## 🔍 Proxy Pattern Types

### 1. Virtual Proxy
- **Purpose**: Lazy initialization of expensive objects
- **Example**: Loading large images only when needed

### 2. Remote Proxy
- **Purpose**: Local representation of remote objects
- **Example**: RMI, CORBA, web services

### 3. Protection Proxy
- **Purpose**: Access control and security
- **Example**: File access control, database permissions

### 4. Smart Proxy
- **Purpose**: Additional functionality (caching, logging, reference counting)
- **Example**: Object caching, access logging

### 5. Cache Proxy
- **Purpose**: Caching expensive operations
- **Example**: Database query results, API responses

## 🔍 Best Practices

- **Interface Segregation**: Keep the Subject interface minimal and focused
- **Single Responsibility**: Each proxy should have one clear purpose
- **Transparency**: Proxy should be transparent to the client
- **Error Handling**: Implement proper error handling and fallback mechanisms
- **Performance**: Consider the overhead of proxy operations
- **Thread Safety**: Ensure proxy operations are thread-safe if needed

## 🚨 Common Pitfalls

- **Over-engineering**: Don't use proxy for simple cases where direct access is sufficient
- **Performance Overhead**: Be aware of the additional overhead proxy introduces
- **Complexity**: Too many proxy layers can make the system hard to understand
- **Memory Leaks**: Ensure proper cleanup of cached objects and references
