# Decorator Design Pattern - Java Implementation

This folder contains a clean, minimal Java implementation of the Decorator pattern, with both a structure-first demo and a practical example.

## Folder Structure

- `Structure/`
  - `Component.java` — Base interface with `operation()`
  - `ConcreteComponent.java` — Core behavior, returns `"Hello"`
  - `Decorator.java` — Abstract wrapper holding a `Component`
  - `ConcreteDecoratorA.java` — Adds `" World"`
  - `ConcreteDecoratorB.java` — Adds `"!"`
  - `Client.java` — Builds compositions and returns output lines
  - `Main.java` — Runs the structure demo
- `Example/`
  - `Notifier.java` — Base interface with `send()`
  - `BasicNotifier.java` — Core behavior, returns `"Notify"`
  - `NotifierDecorator.java` — Abstract notifier wrapper
  - `EmailDecorator.java` — Appends `" via Email"`
  - `SmsDecorator.java` — Appends `" via SMS"`
  - `Client.java` — Builds a notification pipeline
  - `Main.java` — Runs the example demo

## When to Use Decorator

Use Decorator when you need to:
- Add responsibilities to objects dynamically at runtime
- Combine behaviors flexibly without subclass explosion
- Keep single-responsibility small decorators that can be composed

Prefer it over deep inheritance when behaviors are orthogonal and combinable.

## How to Run (Windows cmd)

Run from the project root: `design_patterns_coding`

- Structure demo only:

```bat
cd /d D:\Code\Java\design-pattern\design_patterns_coding
javac -d out src\Creational\Decorator\Java\Structure\*.java
java -cp out Creational.Decorator.Java.Structure.Main
```

- Example demo (compiles both Structure and Example):

```bat
cd /d D:\Code\Java\design-pattern\design_patterns_coding
javac -d out src\Creational\Decorator\Java\Structure\*.java src\Creational\Decorator\Java\Example\*.java
java -cp out Creational.Decorator.Java.Example.Main
```

Tip: You can compile both once, then run either main class as needed with `java -cp out <main-class>`.

## Expected Output

- Structure/Main

```
Hello
Hello World
Hello World!
```

- Example/Main

```
Notify
Notify via Email
Notify via Email via SMS
```

## Notes

- Outputs are derived directly from the source: decorators concatenate small strings to show how behavior is layered.
- Packages are set, so prefer compiling from the project root with `-d out` and running with `-cp out` as shown above.

