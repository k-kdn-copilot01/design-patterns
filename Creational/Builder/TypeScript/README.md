# Builder Pattern - TypeScript

## Overview

Builder is a design pattern belonging to the Creational Patterns group, which allows building complex objects step by step in an organized manner. This pattern separates the construction of complex objects from their representation, allowing the same construction process to create different representations.

## Pattern Structure

### Core Components

1. **Product** - The complex object being built
2. **Builder** - Abstract interface that defines construction steps
3. **ConcreteBuilder** - Concrete implementations of Builder
4. **Director** - Controls the construction process, defines the order of steps
5. **Client** - Uses Director and Builder to create products

### Directory Structure

```
TypeScript/
├── Structure/              # Core pattern implementation
│   ├── Product.ts          # Product class
│   ├── Builder.ts          # Abstract Builder interface
│   ├── ConcreteBuilder1.ts # Concrete Builder implementation
│   ├── ConcreteBuilder2.ts # Another Concrete Builder
│   ├── Director.ts         # Director class
│   ├── Client.ts           # Client code
│   └── Main.ts            # Structure demo
├── Example/               # Real-world example
│   ├── Meal.ts            # Product (Meal)
│   ├── MealBuilder.ts     # Abstract Builder
│   ├── ItalianMealBuilder.ts
│   ├── AsianMealBuilder.ts
│   ├── Chef.ts            # Director
│   ├── Restaurant.ts      # Client
│   └── Main.ts           # Example demo
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
cd Creational/Builder/TypeScript
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
=== Builder Pattern Demo ===

--- Individual Product Creation ---
Minimal product (Builder 1): Product(PartA1)
Parts: Product parts: PartA1
Part count: 1

Full product (Builder 2): Product(PartA2, PartB2, PartC2)
Parts: Product parts: PartA2, PartB2, PartC2
Part count: 3

Custom product (Builder 1, A+B): Product(PartA1, PartB1)
Parts: Product parts: PartA1, PartB1

==================================================

--- Multiple Product Creation ---

--- Building with Builder 1 ---
Minimal product: Product(PartA1)
Full product: Product(PartA1, PartB1, PartC1)
Custom product (A, C): Product(PartA1, PartC1)

--- Building with Builder 2 ---
Minimal product: Product(PartA2)
Full product: Product(PartA2, PartB2, PartC2)
Custom product (A, C): Product(PartA2, PartC2)

Total products created: 6

==================================================

--- Builder Comparison ---
Builder Comparison:
Builder 1 Product: Product(PartA1, PartB1, PartC1)
Builder 2 Product: Product(PartA2, PartB2, PartC2)
Same parts: false
Part count difference: 0

==================================================

--- Step-by-Step Building Process ---
Building product step by step with Builder 1:
Step 1: Building part A...
Current product: Product(PartA1)
Step 2: Building part B...
Current product: Product(PartA1, PartB1)
Step 3: Building part C...
Final product: Product(PartA1, PartB1, PartC1)
Final parts: Product parts: PartA1, PartB1, PartC1

==================================================

--- Builder Reuse ---
Using same builder multiple times:
Build 1: Product(PartA1, PartB1, PartC1)
Build 2: Product(PartA1, PartB1, PartC1)
Build 3: Product(PartA1, PartB1, PartC1)

✓ Builder can be reused multiple times
✓ Each build creates a fresh product
✓ Director manages the construction process
```

### Example Demo Output

```
=== Builder Pattern - Meal Construction Example ===

--- Individual Meal Creation ---
Light Italian Meal:
Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Beverage: Chianti Wine
Price: $23

Full Asian Meal:
Appetizer: Spring Rolls with sweet chili sauce
Main Course: Teriyaki Chicken with rice
Side Dish: Miso Soup
Dessert: Mango Sticky Rice
Beverage: Green Tea
Price: $37

Custom Italian Meal (Appetizer + Main + Dessert):
Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Dessert: Tiramisu
Price: $26

Special Asian Meal with Extras:
Appetizer: Spring Rolls with sweet chili sauce
Main Course: Teriyaki Chicken with rice
Side Dish: Miso Soup
Dessert: Mango Sticky Rice
Beverage: Green Tea
Extras: Extra soy sauce, Chopsticks, Fortune cookie
Price: $43

============================================================

--- Multiple Meal Creation ---

--- Creating Meal 1 ---
Light meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Beverage: Chianti Wine
Price: $23

Full meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $37

Custom meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Dessert: Tiramisu
Price: $26

--- Creating Meal 2 ---
Light meal: Appetizer: Spring Rolls with sweet chili sauce
Main Course: Teriyaki Chicken with rice
Beverage: Green Tea
Price: $23

Full meal: Appetizer: Spring Rolls with sweet chili sauce
Main Course: Teriyaki Chicken with rice
Side Dish: Miso Soup
Dessert: Mango Sticky Rice
Beverage: Green Tea
Price: $37

Custom meal: Appetizer: Spring Rolls with sweet chili sauce
Main Course: Teriyaki Chicken with rice
Dessert: Mango Sticky Rice
Price: $26

Total meals created: 6

============================================================

--- Builder Comparison ---
Builder Comparison:
Builder 1 Meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $37

Builder 2 Meal: Appetizer: Spring Rolls with sweet chili sauce
Main Course: Teriyaki Chicken with rice
Side Dish: Miso Soup
Dessert: Mango Sticky Rice
Beverage: Green Tea
Price: $37

Price difference: $0

============================================================

--- Step-by-Step Meal Building Process ---
Building Italian meal step by step:
Step 1: Building appetizer...
Current meal: Appetizer: Bruschetta with tomatoes and basil
Step 2: Building main course...
Current meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Step 3: Building side dish...
Current meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Step 4: Building dessert...
Current meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Step 5: Building beverage...
Final meal: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Final price: $37

============================================================

--- Builder Reuse ---
Using same builder multiple times:
Build 1: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $37

Build 2: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $37

Build 3: Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $37

✓ Builder can be reused multiple times
✓ Each build creates a fresh meal
✓ Chef manages the construction process

============================================================

--- Restaurant Statistics ---
Restaurant Statistics:
Total Orders: 10
Total Revenue: $320
Average Order Price: $32.00

============================================================

--- Different Meal Configurations ---

--- Quick Lunch ---
Main Course: Spaghetti Carbonara
Beverage: Chianti Wine
Price: $18

--- Business Dinner ---
Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $37

--- Date Night ---
Appetizer: Bruschetta with tomatoes and basil
Main Course: Spaghetti Carbonara
Dessert: Tiramisu
Beverage: Chianti Wine
Price: $26

--- Family Meal ---
Main Course: Spaghetti Carbonara
Side Dish: Caesar Salad
Beverage: Chianti Wine
Price: $26
```

## Advantages of Builder Pattern

1. **Step-by-step Construction**: Build objects step by step in an organized manner
2. **Reusable Builders**: Can reuse builders for multiple products
3. **Flexible Construction**: Can create different variants of the same product
4. **Separation of Concerns**: Separates construction logic from usage logic
5. **Director Control**: Director can control the construction process
6. **Complex Object Creation**: Easy to create complex objects with many properties

## When to Use

- When you need to create complex objects with many properties
- When you want to separate construction process from representation
- When you need to create multiple variants of the same object
- When object creation is complex and needs step-by-step control
- When you want to reuse construction processes for different objects

## Comparison with Other Patterns

- **vs Factory Method**: Builder constructs step by step, Factory Method creates complete objects
- **vs Abstract Factory**: Builder creates one complex object, Abstract Factory creates families of objects
- **vs Prototype**: Builder constructs new, Prototype copies from existing templates
- **vs Singleton**: Builder creates multiple instances, Singleton ensures single instance

## Best Practices

1. **Clear Builder Interface**: Define clear interface for construction steps
2. **Director Management**: Use Director to manage construction process
3. **Builder Reuse**: Design builders that can be reused
4. **Validation**: Add validation for construction steps
5. **Fluent Interface**: Consider using method chaining for builders
6. **Error Handling**: Handle errors when required steps are missing

## Fluent Builder Pattern (Optional Enhancement)

You can extend the Builder pattern with Fluent Interface:

```typescript
class FluentMealBuilder extends MealBuilder {
  buildAppetizer(): this {
    this.meal.setAppetizer("Bruschetta");
    return this; // Return this for chaining
  }

  buildMainCourse(): this {
    this.meal.setMainCourse("Pasta");
    return this;
  }
}

// Usage
const meal = new FluentMealBuilder()
  .buildAppetizer()
  .buildMainCourse()
  .buildBeverage()
  .getMeal();
```
