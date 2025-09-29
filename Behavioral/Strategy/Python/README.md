# Strategy Design Pattern - Python Implementation

This folder contains Python implementations of the **Strategy** design pattern, demonstrating the pattern structure and a real-world payment processing example.

## 📁 Folder Structure

- `Structure/`
  - `Strategy.py` — Abstract base class defining the strategy interface
  - `ConcreteStrategyA.py` — Concrete implementation of Strategy A
  - `ConcreteStrategyB.py` — Concrete implementation of Strategy B
  - `Context.py` — Context class that uses strategies
  - `Main.py` — Demo for structure-only implementations
- `Example/`
  - `PaymentStrategy.py` — Abstract base class for payment strategies
  - `CreditCardPayment.py` — Credit card payment implementation
  - `PayPalPayment.py` — PayPal payment implementation
  - `BankTransferPayment.py` — Bank transfer payment implementation
  - `PaymentProcessor.py` — Context class for payment processing
  - `Main.py` — Demo using real-world payment processing scenario
- `README.md` — This documentation

## 🎯 When to Use Strategy Pattern

The Strategy pattern should be used when:

- You have multiple ways to perform a task and want to choose the algorithm at runtime
- You want to avoid conditional statements for algorithm selection
- You need to add new algorithms without modifying existing code
- You want to isolate algorithm implementation details from client code
- You have a family of related algorithms that can be used interchangeably

## 🏗️ Pattern Structure

### Core Components

1. **Strategy Interface** (`Strategy.py`)
   - Defines the common interface for all concrete strategies
   - Contains abstract methods that concrete strategies must implement

2. **Concrete Strategies** (`ConcreteStrategyA.py`, `ConcreteStrategyB.py`)
   - Implement the strategy interface
   - Each contains a specific algorithm implementation
   - Are interchangeable at runtime

3. **Context** (`Context.py`)
   - Maintains a reference to a strategy object
   - Delegates work to the strategy object
   - Can change strategies at runtime

### Class Diagram
```
Strategy (interface)
    ↑
    ├── ConcreteStrategyA
    └── ConcreteStrategyB

Context
    ↓ uses
Strategy
```

## 🚀 How to Run

### 1. Structure Demo (Basic Pattern Implementation)

```bash
cd Behavioral/Strategy/Python/Structure
python Main.py
```

**Expected Output:**
```
=== Structure Demo: Strategy Pattern ===

1. Using Strategy A:
Strategy A: Processing 'Sample Data' with algorithm A
Result: Strategy A: Processing 'Sample Data' with algorithm A

2. Switching to Strategy B:
Strategy B: Processing 'Sample Data' with algorithm B
Result: Strategy B: Processing 'Sample Data' with algorithm B

3. Demonstrating strategy interchangeability:
   Strategy 1 result: Strategy A: Processing 'Data 1' with algorithm A
   Strategy 2 result: Strategy B: Processing 'Data 2' with algorithm B

=== Structure Demo Complete ===
```

### 2. Example Demo (Real-World Payment Processing)

```bash
cd Behavioral/Strategy/Python/Example
python Main.py
```

**Expected Output:**
```
=== Strategy Pattern Demo: Payment Processing System ===

🛒 Shopping Cart Checkout Simulation

1. Customer chooses Credit Card payment:
Payment method changed to: Credit Card

--- Processing Payment ---
Amount: $99.99
Method: Credit Card
Processing credit card payment of $99.99
Card: ****-****-****-3456
CVV: 123
Expiry: 12/25
✅ Credit card payment successful! Transaction ID: CC_1695998400
--- Payment Complete ---

2. Customer switches to PayPal payment:
Payment method changed to: PayPal

--- Processing Payment ---
Amount: $49.50
Method: PayPal
Processing PayPal payment of $49.50
PayPal Email: user@example.com
✅ PayPal payment successful! Transaction ID: PP_1695998401
--- Payment Complete ---

3. Customer chooses Bank Transfer for large purchase:
Payment method changed to: Bank Transfer

--- Processing Payment ---
Amount: $500.00
Method: Bank Transfer
Processing bank transfer of $500.00
Account: ****4321
Routing: 123456789
✅ Bank transfer successful! Transaction ID: BT_1695998402
--- Payment Complete ---

4. Processing multiple orders with different payment methods:
Payment method changed to: Credit Card

--- Processing Payment ---
Amount: $25.99
Method: Credit Card
Processing credit card payment of $25.99
Card: ****-****-****-3456
CVV: 123
Expiry: 12/25
✅ Credit card payment successful! Transaction ID: CC_1695998403
--- Payment Complete ---

Payment method changed to: PayPal

--- Processing Payment ---
Amount: $75.00
Method: PayPal
Processing PayPal payment of $75.00
PayPal Email: user@example.com
✅ PayPal payment successful! Transaction ID: PP_1695998404
--- Payment Complete ---

Payment method changed to: Bank Transfer

--- Processing Payment ---
Amount: $200.00
Method: Bank Transfer
Processing bank transfer of $200.00
Account: ****4321
Routing: 123456789
✅ Bank transfer successful! Transaction ID: BT_1695998405
--- Payment Complete ---

📊 Payment Summary:
==================================================
Total transactions: 6
Total amount paid: $950.48

Transaction Details:
  1. credit_card: $99.99 - CC_1695998400
  2. paypal: $49.50 - PP_1695998401
  3. bank_transfer: $500.00 - BT_1695998402
  4. credit_card: $25.99 - CC_1695998403
  5. paypal: $75.00 - PP_1695998404
  6. bank_transfer: $200.00 - BT_1695998405

=== Demo Complete ===

💡 Key Benefits of Strategy Pattern:
   • Easy to add new payment methods
   • Runtime strategy switching
   • Clean separation of payment logic
   • Each payment method is independently testable
```

## 🎓 Key Learning Points

### 1. **Runtime Strategy Selection**
The Context class can change strategies at runtime using `set_strategy()`, demonstrating the flexibility of the pattern.

### 2. **Algorithm Encapsulation**
Each strategy encapsulates a specific algorithm, making the code more modular and maintainable.

### 3. **Open/Closed Principle**
New strategies can be added without modifying existing code, following the Open/Closed Principle.

### 4. **Single Responsibility**
Each strategy class has a single responsibility: implementing one specific algorithm.

### 5. **Polymorphism**
The Context class works with any strategy through the common Strategy interface, demonstrating polymorphism.

## 🔍 Real-World Applications

The Strategy pattern is commonly used in:

- **Payment Processing**: Different payment methods (credit card, PayPal, bank transfer)
- **Sorting Algorithms**: Different sorting strategies (quick sort, merge sort, bubble sort)
- **Compression**: Different compression algorithms (ZIP, RAR, 7Z)
- **Validation**: Different validation rules for different data types
- **Pricing**: Different pricing strategies (discount, premium, bulk pricing)
- **Authentication**: Different authentication methods (OAuth, JWT, session-based)

## 🏆 Benefits

- **Flexibility**: Easy to switch between algorithms at runtime
- **Maintainability**: Each strategy is isolated and can be modified independently
- **Extensibility**: New strategies can be added without changing existing code
- **Testability**: Each strategy can be tested independently
- **Code Reuse**: Strategies can be reused across different contexts

## ⚠️ Considerations

- **Increased Complexity**: More classes and interfaces compared to simple conditional logic
- **Client Awareness**: Clients must be aware of different strategies
- **Strategy Selection**: Need a mechanism to select appropriate strategies

## 🔧 Best Practices

1. **Keep Strategies Simple**: Each strategy should focus on one algorithm
2. **Use Meaningful Names**: Strategy names should clearly indicate their purpose
3. **Consider Strategy Selection**: Implement a factory or registry for strategy selection
4. **Handle Strategy State**: Be careful with stateful strategies
5. **Document Strategy Behavior**: Clearly document what each strategy does

## 📚 Related Patterns

- **State Pattern**: Similar structure but different intent (state vs. algorithm)
- **Template Method**: Defines algorithm skeleton with customizable steps
- **Command Pattern**: Encapsulates requests as objects
- **Factory Method**: Creates objects without specifying their exact classes
