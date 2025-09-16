# Prototype Pattern - TypeScript

## Overview

Prototype is a design pattern belonging to the Creational Patterns group, which allows creating new objects by cloning existing objects instead of creating them from scratch. This pattern is particularly useful when object creation is expensive or when you need to create many variants of the same type of object.

## Pattern Structure

### Core Components

1. **Prototype** - Interface that defines the `clone()` method for object copying
2. **ConcretePrototype** - Concrete implementations of Prototype that implement clone logic
3. **Client** - Uses Prototype to create copies instead of creating new ones from scratch

### Directory Structure

```
TypeScript/
├── Structure/              # Core pattern implementation
│   ├── Prototype.ts        # Prototype interface
│   ├── ConcretePrototypeA.ts
│   ├── ConcretePrototypeB.ts
│   ├── Client.ts           # Client code
│   └── Main.ts            # Structure demo
├── Example/               # Real-world example
│   ├── Document.ts        # Abstract Document (Prototype)
│   ├── ReportDocument.ts  # Concrete Document
│   ├── ConfigurationDocument.ts
│   ├── DocumentRegistry.ts
│   ├── DocumentManager.ts
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
cd Creational/Prototype/TypeScript
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
=== Prototype Pattern Demo ===

--- Testing ConcretePrototypeA ---
Original: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"nested value"})
Shallow clone: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"nested value"})
Deep clone: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"nested value"})
Reference comparison:
- Same reference: false
- Same type: true
- Same content: true
Cloning comparison:
- Shallow clone nested reference same: true
- Deep clone nested reference same: false

--- Modifying nested object ---
Original after modification: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"modified value"})
Shallow clone after original modification: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"modified value"})
Deep clone after original modification: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"nested value"})

==================================================

--- Testing ConcretePrototypeB ---
Original: ConcretePrototypeB(name="Document B", items=["item1", "item2"], metadata={"created":"2024-01-01T00:00:00.000Z","version":2})
Shallow clone: ConcretePrototypeB(name="Document B", items=["item1", "item2"], metadata={"created":"2024-01-01T00:00:00.000Z","version":2})
Deep clone: ConcretePrototypeB(name="Document B", items=["item1", "item2"], metadata={"created":"2024-01-01T00:00:00.000Z","version":2})
Reference comparison:
- Same reference: false
- Same type: true
- Same content: true
Cloning comparison:
- Shallow clone nested reference same: true
- Deep clone nested reference same: false

--- Modifying array ---
Original after adding item: ConcretePrototypeB(name="Document B", items=["item1", "item2", "item3"], metadata={"created":"2024-01-01T00:00:00.000Z","version":2})
Shallow clone after original modification: ConcretePrototypeB(name="Document B", items=["item1", "item2", "item3"], metadata={"created":"2024-01-01T00:00:00.000Z","version":2})
Deep clone after original modification: ConcretePrototypeB(name="Document B", items=["item1", "item2"], metadata={"created":"2024-01-01T00:00:00.000Z","version":2})

==================================================

--- Working with Prototype interface ---

Prototype 1:
Client: Cloned ConcretePrototypeA -> ConcretePrototypeA

Prototype 2:
Client: Cloned ConcretePrototypeB -> ConcretePrototypeB

--- Prototype Registry Demo ---
Available prototypes in registry:
- typeA: ConcretePrototypeA
- typeB: ConcretePrototypeB

Cloning from registry:
Cloned from registry: ConcretePrototypeA(field1="Original A", field2=100, nestedObject={"value":"modified value"})
```

### Example Demo Output

```
=== Prototype Pattern - Document Cloning Example ===

--- Original Prototypes ---
Report Prototype:
Title: Monthly Report Template
Author: System Admin
Version: 1
Tags: [template, monthly]
Report Type: Monthly
Sections: 2
Attachments: 0

Config Prototype:
Title: Application Config Template
Author: DevOps Team
Version: 1
Tags: [config, template]
Environment: production
Dependencies: [express, mongoose]
Settings: {database.host: "localhost", database.port: 5432, api.timeout: 30000}

============================================================

--- Creating Individual Documents ---
January Report:
Title: January 2024 Report
Author: System Admin
Version: 1
Tags: [template, monthly, q1]
Report Type: Monthly
Sections: 3
Attachments: 1

February Report:
Title: February 2024 Report
Author: System Admin
Version: 1
Tags: [template, monthly, q1, progress]
Report Type: Monthly
Sections: 3
Attachments: 1

Production Config:
Title: Production Configuration
Author: DevOps Team
Version: 1
Tags: [config, template, production]
Environment: production
Dependencies: [express, mongoose]
Settings: {database.host: "prod-db.company.com", database.port: 5432, api.timeout: 60000}

Staging Config:
Title: Staging Configuration
Author: DevOps Team
Version: 1
Tags: [config, template, staging]
Environment: staging
Dependencies: [express, mongoose]
Settings: {database.host: "staging-db.company.com", database.port: 5432, api.timeout: 10000}

============================================================

--- Creating Multiple Documents Efficiently ---
Created 3 quarterly reports:

Q1 2024 Report 1:
Title: Q1 2024 Report 1
Author: System Admin
Version: 1
Tags: [template, monthly, month-1]
Report Type: Monthly
Sections: 3
Attachments: 0

Q1 2024 Report 2:
Title: Q1 2024 Report 2
Author: System Admin
Version: 1
Tags: [template, monthly, month-2]
Report Type: Monthly
Sections: 3
Attachments: 0

Q1 2024 Report 3:
Title: Q1 2024 Report 3
Author: System Admin
Version: 1
Tags: [template, monthly, month-3]
Report Type: Monthly
Sections: 3
Attachments: 0

============================================================

--- Demonstrating Reference Independence ---
Before modification:
January tags: [template, monthly, q1]
February tags: [template, monthly, q1, progress]

After modifying January report:
January tags: [template, monthly, q1, modified]
February tags: [template, monthly, q1, progress]
✓ February report is unaffected (independent clone)

============================================================

--- Document Statistics ---
Total documents: 7
Documents by type:
- ReportDocument: 5
- ConfigurationDocument: 2

--- Available Prototype Types ---
- monthly-report: Title: Monthly Report Template
Author: System Admin
Version: 1
Tags: [template, monthly]

- app-config: Title: Application Config Template
Author: DevOps Team
Version: 1
Tags: [config, template]

--- Template Customization Demo ---
Custom Report:
Title: Custom Q4 Report
Author: System Admin
Version: 1
Tags: [template, monthly, year-end, planning]
Report Type: Quarterly
Sections: 4
Attachments: 0
```

## Shallow vs Deep Cloning

### Shallow Cloning

- Only copies first-level properties
- Nested objects still share references
- Faster and uses less memory
- Suitable when you don't need to modify nested objects

### Deep Cloning

- Copies all properties, including nested objects
- Each nested object is completely recreated
- Slower and uses more memory
- Suitable when you need to modify nested objects independently

## Advantages of Prototype Pattern

1. **Performance**: Avoids creating complex objects from scratch
2. **Flexibility**: Easy to create many variants from one prototype
3. **Memory Efficiency**: Can share prototypes between instances
4. **Dynamic Configuration**: Can modify prototypes at runtime
5. **Registry Pattern**: Can manage multiple prototype types

## When to Use

- When object creation is expensive (database queries, network calls)
- When you need to create many similar objects with few changes
- When you want to avoid complex subclassing
- When you need to create objects at runtime based on configuration
- When working with template/document systems

## Comparison with Other Patterns

- **vs Factory Method**: Prototype clones existing objects, Factory Method creates new objects
- **vs Abstract Factory**: Prototype creates objects from templates, Abstract Factory creates families of objects
- **vs Builder**: Prototype copies existing objects, Builder constructs objects step by step
- **vs Singleton**: Prototype creates multiple copies, Singleton ensures single instance

## Best Practices

1. **Implement proper cloning**: Ensure clone method creates complete copies
2. **Choose shallow vs deep**: Decide based on specific use case
3. **Use registry pattern**: Manage prototypes efficiently
4. **Handle circular references**: Be careful with objects that have reference cycles
5. **Consider memory usage**: Deep cloning can use a lot of memory
