# Factory Method Design Pattern - Java Implementation

This folder contains Java implementations of the **Factory Method** design pattern, demonstrating the structural approach and a real-world example.

## 📁 Folder Structure

- `Java/`
  - `Structure/`
    - `Product.java` — Interface defining the product contract
    - `Creator.java` — Abstract creator with factory method
    - `ConcreteCreator1.java` & `ConcreteCreator2.java` — Concrete creators
    - `ConcreteProduct1.java` & `ConcreteProduct2.java` — Concrete products
    - `Main.java` — Demo for structure-only implementations
  - `Example/`
    - `Fruit.java` — Product interface for fruit shop example
    - `Shop.java` — Abstract creator for shop operations
    - `Coconut.java` & `Watermelon.java` — Concrete fruit products
    - `CoconutShop.java` & `WatermelonShop.java` — Concrete shop creators
    - `Main.java` — Real-world fruit shop demonstration
- `README.md` — This documentation

## 🎯 When to Use Factory Method

The Factory Method pattern should be used when:
- You need to **delegate object creation** to subclasses
- You want to **eliminate tight coupling** between creator and concrete products
- You need to **extend product creation** without modifying existing code
- You have a **family of related products** that share common operations
- You want to **encapsulate object creation logic** in separate classes

## 🏗️ Structure vs. Example Implementations

### Structure Implementation (`Structure/`)
```java
// Abstract creator defines the factory method
abstract class Creator {
    public void process() {
        Product product = createProduct(); // Factory method
        product.step1();
        product.step2();
        product.step3();
    }
    abstract Product createProduct(); // Factory method
}
```

**Key Components:**
- **Product Interface**: Defines common operations for all products
- **Creator Abstract Class**: Contains business logic and factory method
- **Concrete Creators**: Implement the factory method to create specific products
- **Concrete Products**: Implement the product interface with specific behavior

### Real-World Example (`Example/`)
```java
// Fruit shop example demonstrating practical usage
abstract class Shop {
    public void sell() {
        Fruit fruit = createFruit(); // Factory method
        fruit.prepareFruit();
        fruit.transferFruit();
        fruit.getMoney();
    }
    abstract Fruit createFruit(); // Factory method
}
```

**Real-World Benefits:**
- **Extensibility**: Adding new fruit types doesn't require changing existing shop logic
- **Separation of Concerns**: Shop operations are separate from fruit creation
- **Polymorphism**: Same selling process works for different fruit types
- **Maintainability**: Easy to add new shops or modify existing ones

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd Creational/Factory/Java/Structure
   javac *.java
   java Main
   ```

2. Demo real-world fruit shop example:
   ```bash
   cd Creational/Factory/Java/Example
   javac *.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)
```
Product 2 - step 1
Product 2 - step 2
Product 2 - step 3
```

## 📊 Expected Output (Example/Main)
```
This coconut come from Asia
I will pick it into the nilon for you
This's just a gift for you
```

## 🎓 Key Learning Points

1. **Factory Method**: The `createProduct()` method delegates object creation to subclasses
2. **Open/Closed Principle**: You can add new products without modifying existing creator code
3. **Polymorphism**: Same business logic works with different product implementations
4. **Encapsulation**: Object creation logic is encapsulated in creator classes
5. **Loose Coupling**: Creator classes don't depend on concrete product classes

## 🔍 Pattern Benefits

### Advantages:
- **Eliminates tight coupling** between creator and product classes
- **Supports Open/Closed Principle** - open for extension, closed for modification
- **Single Responsibility** - each creator is responsible for one product type
- **Consistent interface** - all products follow the same contract
- **Easy to test** - creators and products can be tested independently

### Considerations:
- **Increased complexity** - more classes and inheritance hierarchy
- **Runtime overhead** - slight performance cost due to polymorphism
- **Learning curve** - developers need to understand the pattern structure

## 💡 Real-World Use Cases

- **UI Component Libraries**: Creating different types of buttons, dialogs, or forms
- **Database Connections**: Creating connections for different database types
- **Document Processing**: Creating parsers for different file formats (PDF, Word, Excel)
- **Game Development**: Creating different types of enemies, weapons, or characters
- **Web Services**: Creating different types of response handlers or validators

## 🔧 Best Practices

- **Keep factory methods simple** - focus on object creation, not complex business logic
- **Use meaningful names** - factory method names should clearly indicate what they create
- **Consider using enums** for product type selection in complex scenarios
- **Document dependencies** - clearly specify what each concrete creator requires
- **Test thoroughly** - ensure all creator-product combinations work correctly
- **Follow naming conventions** - use consistent naming patterns across creators and products

## 🚦 Common Pitfalls to Avoid

- **Don't overuse** - simple object creation doesn't always need the Factory pattern
- **Avoid deep inheritance** - keep the creator hierarchy shallow and manageable
- **Don't mix concerns** - keep business logic separate from creation logic
- **Consider performance** - factory method calls add slight overhead compared to direct instantiation