# Abstract Factory Pattern - TypeScript

## Overview

Abstract Factory is a design pattern belonging to the Creational Patterns group, which allows creating families of related objects without specifying their exact concrete classes. This pattern provides an interface for creating families of related objects without depending on specific concrete classes.

## Pattern Structure

### Core Components

1. **AbstractProduct** - Abstract base classes for product families
2. **ConcreteProduct** - Concrete implementations of AbstractProduct
3. **AbstractFactory** - Abstract base class that defines interface for creating products
4. **ConcreteFactory** - Concrete implementations of AbstractFactory
5. **Client** - Uses AbstractFactory to create and work with product families

### Directory Structure

```
TypeScript/
├── Structure/              # Core pattern implementation
│   ├── AbstractProductA.ts # Abstract Product A
│   ├── AbstractProductB.ts # Abstract Product B
│   ├── ConcreteProductA1.ts
│   ├── ConcreteProductA2.ts
│   ├── ConcreteProductB1.ts
│   ├── ConcreteProductB2.ts
│   ├── AbstractFactory.ts  # Abstract Factory
│   ├── ConcreteFactory1.ts
│   ├── ConcreteFactory2.ts
│   ├── Client.ts           # Client code
│   └── Main.ts            # Structure demo
├── Example/               # Real-world example
│   ├── Button.ts          # Abstract Button
│   ├── Checkbox.ts        # Abstract Checkbox
│   ├── MaterialButton.ts
│   ├── MaterialCheckbox.ts
│   ├── FlatButton.ts
│   ├── FlatCheckbox.ts
│   ├── UIFactory.ts       # Abstract UI Factory
│   ├── MaterialUIFactory.ts
│   ├── FlatUIFactory.ts
│   ├── Application.ts     # Client
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
cd Creational/AbstractFactory/TypeScript
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
=== Abstract Factory Pattern Demo ===

--- Individual Factory Usage ---
Working with Family 1:
- Product A: ConcreteProductA1 operation
- Product B: ConcreteProductB1 operation
- Collaboration: ConcreteProductB1 collaborating with ConcreteProductA1
- Family consistency: ✓

Working with Family 2:
- Product A: ConcreteProductA2 operation
- Product B: ConcreteProductB2 operation
- Collaboration: ConcreteProductB2 collaborating with ConcreteProductA2
- Family consistency: ✓

==================================================

--- Factory Comparison ---
Factory Comparison:

--- Factory 1: Family 1 ---
Working with Family 1:
- Product A: ConcreteProductA1 operation
- Product B: ConcreteProductB1 operation
- Collaboration: ConcreteProductB1 collaborating with ConcreteProductA1
- Family consistency: ✓

--- Factory 2: Family 2 ---
Working with Family 2:
- Product A: ConcreteProductA2 operation
- Product B: ConcreteProductB2 operation
- Collaboration: ConcreteProductB2 collaborating with ConcreteProductA2
- Family consistency: ✓

==================================================

--- Family Consistency Check ---
Factory 1:
Family Consistency Check:
- Product A family: Family 1
- Product B family: Family 1
- Consistent: ✓ Yes

Factory 2:
Family Consistency Check:
- Product A family: Family 2
- Product B family: Family 2
- Consistent: ✓ Yes

==================================================

--- Dynamic Factory Switching ---
Initial factory: Family 1
Working with Family 1:
- Product A: ConcreteProductA1 operation
- Product B: ConcreteProductB1 operation
- Collaboration: ConcreteProductB1 collaborating with ConcreteProductA1
- Family consistency: ✓

Switching to Factory 2...
New factory: Family 2
Working with Family 2:
- Product A: ConcreteProductA2 operation
- Product B: ConcreteProductB2 operation
- Collaboration: ConcreteProductB2 collaborating with ConcreteProductA2
- Family consistency: ✓

==================================================

--- Product Creation Details ---

--- Factory 1: Family 1 ---
Created Product A: ConcreteProductA1
- Operation: ConcreteProductA1 operation
- Family: Family 1
Created Product B: ConcreteProductB1
- Operation: ConcreteProductB1 operation
- Family: Family 1
- Collaboration: ConcreteProductB1 collaborating with ConcreteProductA1

--- Factory 2: Family 2 ---
Created Product A: ConcreteProductA2
- Operation: ConcreteProductA2 operation
- Family: Family 2
Created Product B: ConcreteProductB2
- Operation: ConcreteProductB2 operation
- Family: Family 2
- Collaboration: ConcreteProductB2 collaborating with ConcreteProductA2

==================================================

--- Working with Multiple Factories ---

Client 1 (Family 1):
Working with Family 1:
- Product A: ConcreteProductA1 operation
- Product B: ConcreteProductB1 operation
- Collaboration: ConcreteProductB1 collaborating with ConcreteProductA1
- Family consistency: ✓

Client 2 (Family 2):
Working with Family 2:
- Product A: ConcreteProductA2 operation
- Product B: ConcreteProductB2 operation
- Collaboration: ConcreteProductB2 collaborating with ConcreteProductA2
- Family consistency: ✓

✓ Each factory creates a consistent product family
✓ Products from the same family work together seamlessly
✓ Switching factories changes the entire product family
```

### Example Demo Output

```
=== Abstract Factory Pattern - UI Components Example ===

--- Individual Factory Usage ---
Material Design Application:
=== Material Design Application ===

Component 1 (button):
<button class="material-button" style="background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;">Save</button>

Component 2 (button):
<button class="material-button" style="background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;">Cancel</button>

Component 3 (checkbox):
<label class="material-checkbox " style="display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;">
      <input type="checkbox"  />
      <span class="checkmark"></span>
      Remember me
    </label>

Component 4 (checkbox):
<label class="material-checkbox " style="display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;">
      <input type="checkbox"  />
      <span class="checkmark"></span>
      Subscribe to newsletter
    </label>

=== Component Interaction Demo ===

Component 1:
- Click: Material button "Save" clicked with ripple effect
- Style: background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;
- Theme: Material Design

Component 2:
- Click: Material button "Cancel" clicked with ripple effect
- Style: background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;
- Theme: Material Design

Component 3:
- Toggle: Material checkbox "Remember me" checked
- Style: display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;
- Theme: Material Design

Component 4:
- Toggle: Material checkbox "Subscribe to newsletter" checked
- Style: display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;
- Theme: Material Design

Application Statistics:
Design System: Material Design
Theme: Material
Total Components: 4
- Buttons: 2
- Checkboxes: 2

============================================================

Flat Design Application:
=== Flat Design Application ===

Component 1 (button):
<button class="flat-button" style="background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;">Submit</button>

Component 2 (button):
<button class="flat-button" style="background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;">Reset</button>

Component 3 (checkbox):
<label class="flat-checkbox " style="display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;">
      <input type="checkbox"  />
      <span class="checkmark"></span>
      I agree to terms
    </label>

Component 4 (checkbox):
<label class="flat-checkbox " style="display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;">
      <input type="checkbox"  />
      <span class="checkmark"></span>
      Send notifications
    </label>

=== Component Interaction Demo ===

Component 1:
- Click: Flat button "Submit" clicked with smooth transition
- Style: background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;
- Theme: Flat Design

Component 2:
- Click: Flat button "Reset" clicked with smooth transition
- Style: background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;
- Theme: Flat Design

Component 3:
- Toggle: Flat checkbox "I agree to terms" checked
- Style: display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;
- Theme: Flat Design

Component 4:
- Toggle: Flat checkbox "Send notifications" checked
- Style: display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;
- Theme: Flat Design

Application Statistics:
Design System: Flat Design
Theme: Flat
Total Components: 4
- Buttons: 2
- Checkboxes: 2

============================================================

--- Factory Comparison ---

--- Factory 1: Material Design ---
Button: <button class="material-button" style="background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;">Test Button</button>
Button Click: Material button "Test Button" clicked with ripple effect
Checkbox: <label class="material-checkbox checked" style="display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;">
      <input type="checkbox" checked />
      <span class="checkmark"></span>
      Test Checkbox
    </label>
Checkbox Toggle: Material checkbox "Test Checkbox" unchecked
Theme Consistency: ✓

--- Factory 2: Flat Design ---
Button: <button class="flat-button" style="background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;">Test Button</button>
Button Click: Flat button "Test Button" clicked with smooth transition
Checkbox: <label class="flat-checkbox checked" style="display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;">
      <input type="checkbox" checked />
      <span class="checkmark"></span>
      Test Checkbox
    </label>
Checkbox Toggle: Flat checkbox "Test Checkbox" unchecked
Theme Consistency: ✓

============================================================

--- Dynamic Factory Switching ---
Initial Application (Material Design):
Application Statistics:
Design System: Material Design
Theme: Material
Total Components: 2
- Buttons: 1
- Checkboxes: 1

=== Material Design Application ===

Component 1 (button):
<button class="material-button" style="background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;">Initial Button</button>

Component 2 (checkbox):
<label class="material-checkbox " style="display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;">
      <input type="checkbox"  />
      <span class="checkmark"></span>
      Initial Checkbox
    </label>

Switching to Flat Design...
New Application (Flat Design):
Application Statistics:
Design System: Flat Design
Theme: Flat
Total Components: 2
- Buttons: 1
- Checkboxes: 1

=== Flat Design Application ===

Component 1 (button):
<button class="flat-button" style="background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;">New Button</button>

Component 2 (checkbox):
<label class="flat-checkbox " style="display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;">
      <input type="checkbox"  />
      <span class="checkmark"></span>
      New Checkbox
    </label>

============================================================

--- Theme Consistency Check ---
Button Theme: Material Design
Checkbox Theme: Material Design
Themes Match: ✓ Yes
Design System: Material Design

============================================================

--- Multiple Applications Demo ---

--- Application 1 ---
Application Statistics:
Design System: Material Design
Theme: Material
Total Components: 2
- Buttons: 1
- Checkboxes: 1

=== Component Interaction Demo ===

Component 1:
- Click: Material button "Material Design Button" clicked with ripple effect
- Style: background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;
- Theme: Material Design

Component 2:
- Toggle: Material checkbox "Material Design Checkbox" checked
- Style: display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;
- Theme: Material Design

--- Application 2 ---
Application Statistics:
Design System: Flat Design
Theme: Flat
Total Components: 2
- Buttons: 1
- Checkboxes: 1

=== Component Interaction Demo ===

Component 1:
- Click: Flat button "Flat Design Button" clicked with smooth transition
- Style: background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;
- Theme: Flat Design

Component 2:
- Toggle: Flat checkbox "Flat Design Checkbox" checked
- Style: display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;
- Theme: Flat Design

✓ Each factory creates a consistent component family
✓ Components from the same family have matching themes
✓ Switching factories changes the entire component family
✓ All components work together seamlessly within their family
```

## Advantages of Abstract Factory Pattern

1. **Family Consistency**: Ensures all products in the same family are compatible with each other
2. **Easy Switching**: Easy to change entire product family by changing the factory
3. **Loose Coupling**: Client doesn't depend on concrete classes
4. **Open/Closed Principle**: Easy to add new families without modifying existing code
5. **Single Responsibility**: Each factory is only responsible for creating one family
6. **Product Isolation**: Products from different families cannot accidentally mix

## When to Use

- When you need to create families of related objects
- When you want to ensure products in the same family are compatible with each other
- When you need to switch between different product families at runtime
- When you want to separate product creation from product usage
- When working with UI frameworks, database systems, or platform-specific code

## Comparison with Other Patterns

- **vs Factory Method**: Abstract Factory creates families of products, Factory Method creates single products
- **vs Builder**: Abstract Factory creates complete families, Builder constructs single complex objects
- **vs Prototype**: Abstract Factory creates new objects, Prototype clones existing objects
- **vs Singleton**: Abstract Factory creates multiple families, Singleton ensures single instance

## Best Practices

1. **Clear Family Boundaries**: Define clear boundaries between product families
2. **Consistent Interfaces**: Ensure all products in family have consistent interfaces
3. **Factory Registry**: Consider using registry pattern to manage multiple factories
4. **Dependency Injection**: Use dependency injection to provide factories
5. **Error Handling**: Handle errors when factory cannot create products
6. **Documentation**: Document clearly relationships between products in family

## Real-world Applications

- **UI Frameworks**: Material Design vs Flat Design components
- **Database Systems**: MySQL vs PostgreSQL drivers
- **Operating Systems**: Windows vs Linux file systems
- **Game Development**: Different character classes with compatible equipment
- **Cross-platform Apps**: iOS vs Android UI components
