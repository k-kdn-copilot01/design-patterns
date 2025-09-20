# Adapter Design Pattern - Java Implementation

This folder contains Java implementations of the **Adapter** design pattern, demonstrating different approaches and a real-world example.

## 📁 Folder Structure

- `Structure/`
  - `Main.java` — Demo for structure-only implementations
- `Example/`
  - `Main.java` — Demo using Vietnamese-Japanese translation example
- `README.md` — This documentation

## 🎯 When to Use Adapter

The Adapter pattern should be used when:
- You want to use an existing class, but its interface doesn't match what you need
- You want to create a reusable class that cooperates with unrelated or unforeseen classes
- You need to integrate third-party libraries with incompatible interfaces
- You want to provide a unified interface to multiple similar classes

## 🔧 How the Adapter Pattern Works

### Core Components

1. **VietnameseTarget Interface** (`VietnameseTarget.java`)
   - Defines the interface that Vietnamese client expects to work with
   - This is what the Vietnamese client expects to work with

2. **JapaneseAdaptee Class** (`JapaneseAdaptee.java`)
   - Contains useful behavior for receiving messages, but its interface is incompatible
   - The Japanese class that needs to be adapted

3. **JapaneseAdapter Class** (`JapaneseAdapter.java`)
   - Makes the Japanese class compatible with the Vietnamese interface
   - Acts as a translator between Vietnamese and Japanese

### Translation Example
```java
// Vietnamese client uses the VietnameseTarget interface
VietnameseTarget client = new JapaneseAdapter(new JapaneseAdaptee());
client.send("Xin Chao"); // This gets translated and sent to Japanese adaptee
```

## 🌏 Real-World Example: Vietnamese-Japanese Translation

The example demonstrates a translation system that allows Vietnamese clients to communicate with Japanese systems:

### Translation Components

1. **VietnameseTarget Interface** - Interface that Vietnamese clients expect to use
2. **JapaneseAdaptee Class** - Japanese system that can receive messages
3. **JapaneseAdapter Class** - Translator that converts Vietnamese messages to Japanese format
4. **Main Class** - Demo showing how Vietnamese client communicates with Japanese system

### How It Works
```java
VietnameseTarget client = new JapaneseAdapter(new JapaneseAdaptee());
client.send("Xin Chao"); // Vietnamese message gets translated and sent to Japanese system
```

## 🚀 How to Run

Demo Vietnamese-Japanese translation example:
```bash
cd Example
javac *.java
java Main
```

## 📊 Expected Output
```
Vietnamese message: Xin Chao
Japanese Adaptee received: xin chao
```

## 🎓 Key Learning Points

1. **Interface Compatibility**: The Adapter makes Vietnamese and Japanese interfaces work together
2. **Translation Layer**: The adapter acts as a translator between different languages/systems
3. **Transparency**: The Vietnamese client doesn't know it's using a Japanese system
4. **Flexibility**: Easy to add support for new languages by creating new adapters

## 🔍 Best Practices

- **Single Responsibility**: Each adapter should handle one specific adaptation
- **Interface Segregation**: Keep target interfaces focused and minimal
- **Composition over Inheritance**: Use composition to wrap the adaptee
- **Error Handling**: Handle cases where adaptation isn't possible
- **Documentation**: Clearly document what each adapter does