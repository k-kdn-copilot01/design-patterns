# Factory Method Design Pattern - Java Implementation

This folder contains Java implementation of the **Factory Method** design pattern, demonstrating the creation of objects without specifying their exact classes.

## 📁 Files Overview

- **`Transport.java`** - Product interface defining common methods for all transport types
- **`Truck.java`** - ConcreteProduct for road transport
- **`Ship.java`** - ConcreteProduct for sea transport  
- **`Logistics.java`** - Abstract Creator class with factory method
- **`RoadLogistics.java`** - ConcreteCreator for creating trucks
- **`SeaLogistics.java`** - ConcreteCreator for creating ships
- **`Main.java`** - Demo class showing pattern usage
- **`README.md`** - This documentation

## 🎯 When to Use Factory Method

The Factory Method pattern should be used when:
- You need to **defer instantiation** to subclasses
- You want **loose coupling** between Creator and Product classes
- You have a **family of related products** that share a common interface
- You want to **extend the product creation** without modifying existing code
- The exact type of object to create should be determined at **runtime**

## 🏗️ Pattern Structure

```
Creator (Logistics)
├── + createTransport(): Transport  [Factory Method]
├── + planDelivery(): void         [Business Logic]
└── + getLogisticsType(): String

ConcreteCreator (RoadLogistics, SeaLogistics)
├── + createTransport(): Transport [Override Factory Method]
└── + getLogisticsType(): String   [Override]

Product (Transport)
├── + deliver(): void
├── + getTransportType(): String
└── + getCost(): double

ConcreteProduct (Truck, Ship)
├── + deliver(): void              [Implementation]
├── + getTransportType(): String   [Implementation]
└── + getCost(): double            [Implementation]
```

## 🔄 How It Works

1. **Client** creates a ConcreteCreator (e.g., `RoadLogistics`)
2. **Client** calls business method (e.g., `planDelivery()`)
3. **Creator** calls factory method (`createTransport()`)
4. **ConcreteCreator** overrides factory method to return specific product
5. **Business logic** works with Product interface, not concrete classes

## ⚖️ Factory Method vs Simple Factory vs Abstract Factory

### Factory Method (This Implementation)
```java
// Creator decides which product to create
public abstract class Logistics {
    public abstract Transport createTransport(); // Factory Method
}
```

**Pros:**
- **Extensible** - Easy to add new product types
- **Loose coupling** - Creator doesn't know concrete product classes
- **Single Responsibility** - Each creator handles one product type
- **Open/Closed Principle** - Open for extension, closed for modification

**Cons:**
- **More complex** - Requires inheritance hierarchy
- **More classes** - Need ConcreteCreator for each product type

### Simple Factory (Alternative Approach)
```java
// Single factory class with conditional logic
public class TransportFactory {
    public static Transport createTransport(String type) {
        if (type.equals("truck")) return new Truck();
        if (type.equals("ship")) return new Ship();
        return null;
    }
}
```

**Pros:**
- **Simple** - Only one factory class
- **Centralized** - All creation logic in one place

**Cons:**
- **Violates Open/Closed** - Must modify factory for new products
- **Tight coupling** - Factory knows all concrete products

### Abstract Factory (For Product Families)
```java
// Creates families of related products
public interface LogisticsFactory {
    Transport createTransport();
    Vehicle createVehicle();
    Route createRoute();
}
```

**Use when:** You need to create **families of related products**

## 🚀 How to Run

1. **Compile all Java files:**
   ```bash
   javac *.java
   ```

2. **Run the demo:**
   ```bash
   java Main
   ```

## 📊 Expected Output

```
=== Factory Method Design Pattern Demo ===

1. Testing Road Logistics:
Planning delivery using Road Logistics...
🏭 RoadLogistics factory creating truck...
Truck instance created
Transport type: Road Transport (Truck)
Estimated cost: $100.0
🚛 Delivering goods by TRUCK on the road
   - Loading cargo into truck container
   - Driving on highway network
   - Delivery completed at destination
Delivery planning completed!

2. Testing Sea Logistics:
Planning delivery using Sea Logistics...
🏭 SeaLogistics factory creating ship...
Ship instance created
Transport type: Sea Transport (Ship)
Estimated cost: $250.0
🚢 Delivering goods by SHIP across the ocean
   - Loading cargo into ship containers
   - Navigating through sea routes
   - Delivery completed at port destination
Delivery planning completed!

3. Comparing Transport Types:
🏭 RoadLogistics factory creating truck...
Truck instance created
🏭 SeaLogistics factory creating ship...
Ship instance created
Road transport: Road Transport (Truck) (Cost: $100.0)
Sea transport: Sea Transport (Ship) (Cost: $250.0)
Are they the same type? false

4. Demonstrating Polymorphism:
Performing delivery with: Road Logistics
🏭 RoadLogistics factory creating truck...
Truck instance created
🚛 Delivering goods by TRUCK on the road
   - Loading cargo into truck container
   - Driving on highway network
   - Delivery completed at destination

Performing delivery with: Sea Logistics
🏭 SeaLogistics factory creating ship...
Ship instance created
🚢 Delivering goods by SHIP across the ocean
   - Loading cargo into ship containers
   - Navigating through sea routes
   - Delivery completed at port destination

=== Demo Complete ===
```

## 🎓 Key Learning Points

1. **Polymorphism**: Different creators produce different products, but client uses same interface
2. **Extensibility**: Adding new transport types only requires new ConcreteCreator and ConcreteProduct
3. **Decoupling**: Business logic in `Logistics.planDelivery()` doesn't know concrete product types
4. **Factory Method**: Each ConcreteCreator decides which ConcreteProduct to instantiate
5. **Code Reuse**: Common business logic is inherited from abstract Creator

## 🔍 Real-World Examples

- **GUI Components**: Button factory creating Windows/Mac/Linux buttons
- **Database Drivers**: Connection factory creating MySQL/PostgreSQL/Oracle connections
- **Document Processing**: Document factory creating PDF/Word/Excel processors
- **Payment Processing**: Payment factory creating PayPal/Stripe/Card processors
- **Notification System**: Notification factory creating Email/SMS/Push notifications

## 💡 Best Practices

- **Use interfaces** for Products to ensure loose coupling
- **Keep factory methods simple** - avoid complex logic in creation
- **Consider parameterized factory methods** if you need variants of the same product type
- **Use Abstract Factory** when you need to create families of related products
- **Use Simple Factory** for simple scenarios without need for extension
- **Follow naming conventions**: `createXXX()` for factory methods