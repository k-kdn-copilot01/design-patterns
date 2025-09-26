# Proxy Design Pattern - Java Implementation

This folder contains Java implementations of the **Proxy** design pattern, demonstrating different approaches and a real-world example.

## 📁 Folder Structure

- `Structure/`
  - `Main.java` — All structure classes in one file (100 lines)
- `Example/`
  - `Main.java` — All example classes in one file (93 lines)
- `README.md` — This documentation

## 🎯 When to Use Proxy

The Proxy pattern should be used when:
- You need to control access to an object
- You want to add functionality before/after accessing an object
- You need lazy initialization of expensive objects
- You want to provide a placeholder for a remote object
- You need to add security, caching, or logging functionality

## ⚖️ Virtual vs. Protection Proxy

### Virtual Proxy (`Structure/Main.java`)
```java
// Object created only when first accessed
if (realSubject == null) {
    realSubject = new RealSubject();
}
```

**Pros:**
- Memory efficient - object created only when needed
- Faster application startup
- Transparent to client

**Cons:**
- Slightly slower first access due to object creation
- More complex implementation

### Protection Proxy (`Structure/Main.java`)
```java
// Access control before delegating to real subject
if (hasAccess) {
    realSubject.request();
} else {
    System.out.println("Access denied");
}
```

**Pros:**
- Security control
- Access logging
- Transparent to client

**Cons:**
- Additional overhead for access checks
- More complex implementation

### Real-World Proxy (`Example/Main.java`)
```java
// Lazy loading of expensive image resources
public void display() {
    if (realImage == null) {
        realImage = new RealImage(filename);
    }
    realImage.display();
}
```

**Pros:**
- Lazy loading of expensive resources
- Memory efficient
- Better user experience

**Cons:**
- Slightly slower first access
- More complex implementation

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Structural/Proxy/Java/Structure
   javac Main.java
   java Main
   ```

2. Demo example with structure classes:
   ```bash
   cd Structural/Proxy/Java/Example
   javac Main.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
=== Structure Demo: Proxy Implementations ===

1. Virtual Proxy:
RealSubject created
VirtualProxy: Request processed by RealSubject
VirtualProxy: Request processed by RealSubject

2. Protection Proxy:
Access granted
ProtectionProxy: Request processed by RealSubject
Access denied
ProtectionProxy: Access denied

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/Main)
```
=== Proxy Design Pattern Demo ===

1. Testing Image Proxy (Lazy Loading):
ImageProxy created for: sample.jpg
Loading image: sample.jpg from disk...
Image loaded: sample.jpg
Displaying image: sample.jpg

Second display call (uses cached image):
Displaying image: sample.jpg

2. Testing Multiple Images:
ImageProxy created for: image1.jpg
ImageProxy created for: image2.jpg
Displaying image1:
Loading image: image1.jpg from disk...
Image loaded: image1.jpg
Displaying image: image1.jpg
Displaying image2:
Loading image: image2.jpg from disk...
Image loaded: image2.jpg
Displaying image: image2.jpg

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Lazy Loading**: Virtual proxy creates objects only when needed
2. **Access Control**: Protection proxy controls access to real objects
3. **Transparency**: Client doesn't know it's using a proxy
4. **Delegation**: Proxy delegates requests to real objects

## 🔍 Best Practices

- Use **Virtual Proxy** for expensive object creation
- Use **Protection Proxy** for access control and security
- Use **Remote Proxy** for network objects
- Use **Smart Proxy** for additional functionality like caching
- Keep proxy interface identical to real subject interface
