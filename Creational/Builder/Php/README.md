# Builder Design Pattern - PHP Implementation

This folder contains a sample implementation of the **Builder** pattern in PHP with two parts: `Structure/` (core skeleton) and `Example/` (real-world scenario).

## 📁 Folder Structure

- `Structure/`
  - `Product.php` — Built product composed of parts
  - `Builder.php` — Interface declaring build steps
  - `ConcreteBuilder.php` — Concrete builder for `Product`
  - `Director.php` — Orchestrates the build sequence
  - `Client.php` — Client using Builder/Director
  - `Main.php` — Structure demo
- `Example/`
  - `Meal.php` — Real product (a meal)
  - `MealBuilder.php` — Builder interface for Meal
  - `HealthyMealBuilder.php` — Builder for healthy meals
  - `FastFoodMealBuilder.php` — Builder for fast-food meals
  - `MealDirector.php` — Director for meal building
  - `Main.php` — Real-world demo

## 🎯 When to Use Builder

Use Builder when:
- The object is complex and must be built step by step.
- You want to vary the construction process or swap builders for different variants.
- You want to separate construction from the final representation.

## 🚀 How to Run

1) Structure demo:
```bash
cd Creational/Builder/Php/Structure
php Main.php
```

2) Real-world demo:
```bash
cd Creational/Builder/Php/Example
php Main.php
```

## 📊 Expected Output

### Structure/Main.php
```
=== Structure Demo: Builder Pattern ===

Building Minimal Viable Product...
Product parts: PartA

Building Full Featured Product...
Product parts: PartA, PartB, PartC

Custom build (no Director, client-defined steps)...
Product parts: PartA, PartC

=== Structure Demo Complete ===
```

### Example/Main.php
```
=== Example Demo: Builder Pattern (Meal) ===

1) Healthy Meal via Director (Standard)
Main: Standard Main, Side: Standard Side, Drink: Standard Drink

2) Fast Food Kids Meal via Director
Main: Small Burger, Side: Small Fries, Drink: Juice

3) Custom Healthy Meal (Client-defined)
Main: Grilled Salmon, Side: Quinoa, Drink: Green Tea

=== Example Demo Complete ===
```

## 🧠 Key Takeaways

- **Director** orchestrates build steps and can produce different configurations using the same builder.
- **Builder** hides construction details; swapping builders yields different products.
- **Client** may use the Director or build directly as needed.


