# Builder Design Pattern - Python Implementation

This folder contains Python implementations of the **Builder** design pattern, demonstrating both the basic structure and a real-world house construction example.

## 📁 Folder Structure

- `Structure/`
  - `product.py` — Product class that represents the complex object being built
  - `builder.py` — Abstract Builder interface and Concrete Builder implementations
  - `director.py` — Director class that orchestrates the building process
  - `main.py` — Demo for structure-only implementations
- `Example/`
  - `house.py` — House class representing a complex product with multiple components
  - `house_builder.py` — Abstract HouseBuilder and concrete implementations (Modern, Traditional, Eco-Friendly)
  - `house_director.py` — HouseDirector with different construction sequences
  - `main.py` — Real-world demo using house construction
- `README.md` — This documentation

## 🎯 When to Use Builder

The Builder pattern should be used when:
- You need to construct **complex objects** step by step
- The construction process must allow **different representations** of the same object
- You want to **isolate the construction code** from the representation
- The object has **many optional components** or configurations
- You need to construct objects that require **multiple steps** in a specific order

## 🏗️ Pattern Components

### Core Structure Components

#### 1. **Product** (`product.py`)
```python
class Product:
    def __init__(self):
        self.parts = []
    
    def add_part(self, part: str):
        self.parts.append(part)
```
- Represents the complex object being constructed
- Contains the final result of the building process

#### 2. **Builder** (`builder.py`)
```python
class Builder(ABC):
    @abstractmethod
    def produce_part_a(self) -> None:
        pass
```
- Declares building steps that are common to all builders
- Defines the interface for constructing product parts

#### 3. **ConcreteBuilder** (`builder.py`)
```python
class ConcreteBuilder1(Builder):
    def produce_part_a(self) -> None:
        self._product.add_part("PartA1")
```
- Provides specific implementations of building steps
- Constructs and assembles parts of the product
- Defines and keeps track of the representation it creates

#### 4. **Director** (`director.py`)
```python
class Director:
    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
```
- Constructs objects using the Builder interface
- Defines the order of building steps
- Works with any builder instance

## 🏠 Real-World Example: House Construction

### House Types (ConcreteBuilders)

#### 1. **Modern House**
- Steel frame with glass panels
- Flat roof with solar panels
- Smart windows and automatic doors
- Underground garage and infinity pool

#### 2. **Traditional House**
- Brick walls with wooden trim
- Sloped roof with clay tiles
- Wooden casement windows
- Detached garage and cottage garden

#### 3. **Eco-Friendly House**
- Bamboo and recycled materials
- Green roof with renewable energy
- Triple-glazed windows
- Natural swimming pool and permaculture garden

### Construction Sequences (Director)

- **Basic House**: Foundation + Walls + Roof + Windows + Doors
- **Family House**: Basic + Garage + Garden
- **Luxury House**: Family + Pool

## 🚀 How to Run

1. Demo structure implementations only:
   ```bash
   cd design-patterns/Creational/Builder/Python/Structure
   python main.py
   ```

2. Demo real-world example:
   ```bash
   cd design-patterns/Creational/Builder/Python/Example
   python main.py
   ```

## 📊 Expected Output (Structure/main.py)

```
=== Structure Demo: Builder Pattern ===

Standard basic product (Builder 1):
Product parts: PartA1

Standard full featured product (Builder 1):
Product parts: PartA1, PartB1, PartC1

Standard basic product (Builder 2):
Product parts: PartA2

Standard full featured product (Builder 2):
Product parts: PartA2, PartB2, PartC2

Custom product (without Director):
Product parts: PartA1, PartC1

=== Structure Demo Complete ===
```

## 📊 Expected Output (Example/main.py)

```
=== Example Demo: Builder Pattern - House Construction ===

1. Modern Basic House:
🔨 Building basic house...
✅ Basic house completed!
🏠 House Description:
  • Foundation: Reinforced concrete slab
  • Walls: Steel frame with glass panels
  • Roof: Flat roof with solar panels
  • Windows: Floor-to-ceiling smart windows
  • Doors: Automatic sliding glass doors

2. Traditional Family House:
🔨 Building family house...
✅ Family house completed!
🏠 House Description:
  • Foundation: Stone and mortar foundation
  • Walls: Brick walls with wooden trim
  • Roof: Sloped roof with clay tiles
  • Windows: Wooden frame casement windows
  • Doors: Solid oak doors with brass hardware
  • Garage: Detached 1-car wooden garage
  • Garden: English cottage garden with flowers

3. Eco-Friendly Luxury House:
🔨 Building luxury house...
✅ Luxury house completed!
🏠 House Description:
  • Foundation: Recycled concrete with radiant heating
  • Walls: Bamboo and recycled steel frame with hemp insulation
  • Roof: Green roof with solar panels and wind turbine
  • Windows: Triple-glazed windows with recycled frames
  • Doors: Reclaimed wood doors with natural finish
  • Garage: Electric vehicle charging station
  • Garden: Permaculture garden with rainwater harvesting
  • Pool: Natural swimming pool with biological filtration

4. Custom Modern House (without Director):
🔨 Building custom house...
✅ Custom house completed!
🏠 House Description:
  • Foundation: Reinforced concrete slab
  • Walls: Steel frame with glass panels
  • Roof: Flat roof with solar panels
  • Windows: Floor-to-ceiling smart windows
  • Doors: Automatic sliding glass doors
  • Pool: Infinity pool with LED lighting

5. Comparison - Same Family House, Different Styles:

--- Modern Family House ---
🔨 Building family house...
✅ Family house completed!
🏠 House Description:
  • Foundation: Reinforced concrete slab
  • Walls: Steel frame with glass panels
  • Roof: Flat roof with solar panels
  • Windows: Floor-to-ceiling smart windows
  • Doors: Automatic sliding glass doors
  • Garage: Underground 2-car smart garage
  • Garden: Minimalist zen garden with automated irrigation

--- Traditional Family House ---
🔨 Building family house...
✅ Family house completed!
🏠 House Description:
  • Foundation: Stone and mortar foundation
  • Walls: Brick walls with wooden trim
  • Roof: Sloped roof with clay tiles
  • Windows: Wooden frame casement windows
  • Doors: Solid oak doors with brass hardware
  • Garage: Detached 1-car wooden garage
  • Garden: English cottage garden with flowers

=== Example Demo Complete ===
```

## 🎓 Key Learning Points

1. **Step-by-Step Construction**: The Builder pattern allows you to construct complex objects step by step, rather than all at once
2. **Multiple Representations**: Different builders can create different representations of the same product using identical construction steps
3. **Director Control**: The Director encapsulates construction logic and can create different configurations of the same product
4. **Client Flexibility**: Clients can work directly with builders for custom construction or use directors for standard configurations
5. **Isolation of Concerns**: Construction logic is separated from the product representation

## 🆚 Builder vs. Other Patterns

### Builder vs. Abstract Factory
- **Builder**: Constructs complex objects step by step
- **Abstract Factory**: Creates families of related objects all at once

### Builder vs. Factory Method
- **Builder**: Focuses on how an object is constructed (step-by-step process)
- **Factory Method**: Focuses on what object is created (which class to instantiate)

### Builder vs. Prototype
- **Builder**: Constructs objects from scratch using a step-by-step approach
- **Prototype**: Creates objects by cloning existing instances

## 🔍 Best Practices

- **Use when construction is complex**: Only use Builder when the object construction involves multiple steps or configurations
- **Make builders immutable**: After getting the product, reset the builder to ensure clean state
- **Director is optional**: Clients can work directly with builders for maximum flexibility
- **Fluent interface**: Consider implementing method chaining for more readable code
- **Validation**: Perform validation in the product's constructor or in a separate validation step
- **Thread safety**: Be careful with shared builder instances in multi-threaded environments

## 🔄 Variations

1. **Fluent Builder**: Method chaining for more readable construction
2. **Telescoping Constructor**: Alternative approach using multiple constructors
3. **Step Builder**: Enforces the order of construction steps through type system
4. **Functional Builder**: Uses functions instead of classes for simpler scenarios
