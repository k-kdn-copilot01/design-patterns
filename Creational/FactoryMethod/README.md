# Factory Method Design Pattern - Java Implementation

This folder contains Java implementations of the **Factory Method** design pattern, demonstrating the core structure and a real-world logistics example.

## 📁 Folder Structure

- `Structure/`
  - `Product.java` — Interface defining contract for products
  - `ConcreteProductA.java` — Concrete implementation of Product
  - `ConcreteProductB.java` — Another concrete implementation of Product
  - `Creator.java` — Abstract class containing factory method
  - `ConcreteCreatorA.java` — Concrete creator that creates ConcreteProductA
  - `ConcreteCreatorB.java` — Concrete creator that creates ConcreteProductB
  - `Main.java` — Demo for structure-only implementations
- `Example/`
  - `NotificationService.java` — Product interface (Notification Service)
  - `SmsNotificationService.java` — Concrete product (SMS notifications)
  - `EmailNotificationService.java` — Concrete product (Email notifications)
  - `NotificationManager.java` — Creator abstract class
  - `SmsNotificationManager.java` — Concrete creator for SMS notifications
  - `EmailNotificationManager.java` — Concrete creator for email notifications
  - `Main.java` — Demo using real-world notification service scenario
- `README.md` — This documentation

## 🎯 When to Use Factory Method

The Factory Method pattern should be used when:
- You need to create objects but don't know the exact class beforehand
- You want subclasses to decide which class to instantiate
- You want to separate object creation logic from object usage logic
- You need to easily extend the system with new product types
- You want to follow the **Open/Closed Principle**

## 🏗️ Pattern Structure

### Core Components

1. **Product Interface** (`Product.java`)
   ```java
   public interface Product {
       void doStuff();
   }
   ```

2. **Concrete Products** (`ConcreteProductA.java`, `ConcreteProductB.java`)
   ```java
   public class ConcreteProductA implements Product {
       @Override
       public void doStuff() {
           System.out.println("ConcreteProductA operation");
       }
   }
   ```

3. **Creator Abstract Class** (`Creator.java`)
   ```java
   public abstract class Creator {
       public abstract Product createProduct();
       
       public void someOperation() {
           Product product = createProduct();
           product.doStuff();
       }
   }
   ```

4. **Concrete Creators** (`ConcreteCreatorA.java`, `ConcreteCreatorB.java`)
   ```java
   public class ConcreteCreatorA extends Creator {
       @Override
       public Product createProduct() {
           return new ConcreteProductA();
       }
   }
   ```

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Java/Structure
   javac *.java
   java Main
   ```

2. Demo real-world notification service example:
   ```bash
   cd Java/Example
   javac *.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
=== Factory Method Pattern Demo ===

Using ConcreteCreatorA:
ConcreteProductA operation

Using ConcreteCreatorB:
ConcreteProductB operation

Direct factory method calls:
Product A: ConcreteProductA operation
Product B: ConcreteProductB operation
```

## 📊 Expected Output (Example/Main)
```
=== Factory Method Pattern - Notification Service Example ===

1. SMS Notification:
Notify by SMS: +1234567890 - Alert - Your order has been shipped!

2. Email Notification:
Notify by Email: user@example.com - Welcome - Thank you for joining our service!

3. SMS Length Validation:
Exception caught: Title and content too long
```

## 🎓 Key Learning Points

1. **Polymorphism**: The factory method returns a Product interface, allowing different concrete products
2. **Delegation**: Object creation is delegated to subclasses through the factory method
3. **Flexibility**: Easy to add new product types by creating new concrete creators
4. **Separation of Concerns**: Creation logic is separated from usage logic
5. **Open/Closed Principle**: Open for extension (new creators), closed for modification
6. **Clean Implementation**: Simple, focused example demonstrating core Factory Method concepts
7. **Error Handling**: Shows how validation can be built into concrete products

## ⚖️ Advantages vs Disadvantages

### ✅ Advantages
- **Single Responsibility**: Each creator is responsible for creating one type of product
- **Open/Closed Principle**: Easy to add new product types without modifying existing code
- **Dependency Inversion**: Client code depends on abstractions, not concrete classes
- **Code Reusability**: Common logic is placed in the abstract creator
- **Flexibility**: Runtime decision on which product to create

### ❌ Disadvantages
- **Complexity**: More classes and interfaces compared to direct instantiation
- **Indirection**: Extra layer of abstraction can make code harder to follow
- **Over-engineering**: May be overkill for simple object creation scenarios

## 🔍 Best Practices

- Use **Factory Method** when you have a family of related products
- Keep the factory method **simple** and focused on object creation
- Consider using **Abstract Factory** if you need to create families of related objects
- Use **Simple Factory** for simpler scenarios with fewer product types
- Make sure the **Product interface** is well-designed and stable

## 🌟 Real-World Applications

- **Notification Systems**: Creating different notification channels (SMS, Email, Push)
- **GUI Libraries**: Creating different UI components (buttons, windows, dialogs)
- **Database Drivers**: Creating different database connections
- **Logging Frameworks**: Creating different log appenders
- **Game Development**: Creating different types of game objects
- **E-commerce**: Creating different payment processors
