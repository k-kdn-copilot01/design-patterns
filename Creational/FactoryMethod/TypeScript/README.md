# Factory Method Pattern - TypeScript

## Overview

Factory Method is a design pattern belonging to the Creational Patterns group, which allows creating objects without specifying their exact concrete classes. This pattern uses a factory method to create objects instead of calling the constructor directly.

## Pattern Structure

### Core Components

1. **Product** - Abstract base class that defines the interface for objects being created
2. **ConcreteProduct** - Concrete implementations of Product
3. **Creator** - Abstract base class that defines the factory method
4. **ConcreteCreator** - Concrete implementations of Creator that override the factory method
5. **Client** - Uses Creator to create and work with Product objects

### Directory Structure

```
TypeScript/
├── Structure/           # Core pattern implementation
│   ├── Product.ts       # Abstract Product class
│   ├── ConcreteProductA.ts
│   ├── ConcreteProductB.ts
│   ├── Creator.ts       # Abstract Creator class
│   ├── ConcreteCreatorA.ts
│   ├── ConcreteCreatorB.ts
│   ├── Client.ts        # Client code
│   └── Main.ts         # Structure demo
├── Example/            # Real-world example
│   ├── Transport.ts    # Abstract Transport (Product)
│   ├── Truck.ts        # Concrete Transport
│   ├── Ship.ts         # Concrete Transport
│   ├── Logistics.ts    # Abstract Logistics (Creator)
│   ├── RoadLogistics.ts
│   ├── SeaLogistics.ts
│   ├── LogisticsClient.ts
│   └── Main.ts         # Example demo
├── package.json
├── tsconfig.json
└── README.md
```

## How to Run

### Requirements

- Node.js (v14+)
- npm or yarn

### Install Dependencies

```bash
cd Creational/FactoryMethod/TypeScript
npm install
```

### Run Structure Demo

```bash
npm run start:structure
# or
npm run dev:structure
```

### Run Example Demo

```bash
npm run start:example
# or
npm run dev:example
```

### Build TypeScript

```bash
npm run build
```

## Expected Output

### Structure Demo Output

```
=== Factory Method Pattern Demo ===

Client: Using ConcreteCreatorA:
Creator: ConcreteProductA operation

Client: Using ConcreteCreatorB:
Creator: ConcreteProductB operation

Client: Working with creators through base class:
ConcreteCreatorA: Creator: ConcreteProductA operation
ConcreteCreatorB: Creator: ConcreteProductB operation
```

### Example Demo Output

```
=== Factory Method Pattern - Logistics Example ===

=== Road Logistics ===
Logistics: Planning delivery using Truck
- Method: Delivering goods by road using Truck
- Capacity: 10000 kg
- Speed: 80 km/h
Estimated delivery time: 6.25 hours for 500 km

=== Sea Logistics ===
Logistics: Planning delivery using Ship
- Method: Delivering goods by sea using Ship
- Capacity: 50000 kg
- Speed: 30 km/h
Estimated delivery time: 16.67 hours for 500 km

=== Logistics Comparison ===

--- Road Logistics ---
Logistics: Planning delivery using Truck
- Method: Delivering goods by road using Truck
- Capacity: 10000 kg
- Speed: 80 km/h
Estimated delivery time: 6.25 hours for 500 km

--- Sea Logistics ---
Logistics: Planning delivery using Ship
- Method: Delivering goods by sea using Ship
- Capacity: 50000 kg
- Speed: 30 km/h
Estimated delivery time: 16.67 hours for 500 km

=== Dynamic Logistics Selection ===

--- Option 1: Road Logistics ---
Logistics: Planning delivery using Truck
- Method: Delivering goods by road using Truck
- Capacity: 10000 kg
- Speed: 80 km/h
Estimated delivery time: 6.25 hours for 500 km

--- Option 2: Sea Logistics ---
Logistics: Planning delivery using Ship
- Method: Delivering goods by sea using Ship
- Capacity: 50000 kg
- Speed: 30 km/h
Estimated delivery time: 16.67 hours for 500 km

=== Working with Base Class ===

Road Logistics:
Logistics: Planning delivery using Truck
- Method: Delivering goods by road using Truck
- Capacity: 10000 kg
- Speed: 80 km/h
Estimated delivery time: 6.25 hours for 500 km

Sea Logistics:
Logistics: Planning delivery using Ship
- Method: Delivering goods by sea using Ship
- Capacity: 50000 kg
- Speed: 30 km/h
Estimated delivery time: 16.67 hours for 500 km
```

## Advantages of Factory Method Pattern

1. **Loose Coupling**: Client doesn't depend on concrete classes
2. **Open/Closed Principle**: Easy to add new product types without modifying existing code
3. **Single Responsibility**: Each creator is only responsible for creating one type of product
4. **Polymorphism**: Client can work with products through base class interface

## When to Use

- When you don't know beforehand the exact type of object to create
- When you want subclasses to decide which class to instantiate
- When you want to separate object creation logic from object usage logic
- When you need to provide library/framework for client code

## Comparison with Other Patterns

- **vs Abstract Factory**: Factory Method creates one type of object, Abstract Factory creates families of objects
- **vs Builder**: Factory Method creates complete objects, Builder creates objects step by step
- **vs Prototype**: Factory Method creates new objects, Prototype clones existing objects
