# Factory Method Pattern - Java

Provides a way to delegate object creation to subclasses. The Creator defines the factory method, and ConcreteCreators decide which ConcreteProduct to instantiate.

## Directory structure

```
src/
└── Creational/
    └── FactoryMethod/
        └── Java/
            ├── Structure/
            │   ├── Product.java
            │   ├── ConcreteProduct1.java
            │   ├── ConcreteProduct2.java
            │   ├── Creator.java
            │   ├── ConcreteCreator1.java
            │   ├── ConcreteCreator2.java
            │   ├── Client.java
            │   └── Main.java
            └── Example/
                ├── Transport.java
                ├── Truck.java
                ├── Ship.java
                ├── Logistics.java
                ├── RoadLogistics.java
                ├── SeaLogistics.java
                └── Main.java
```

## How to run

- IntelliJ IDEA
  - Open the project.
  - Right-click `src/Creational/FactoryMethod/Java/Structure/Main.java` → Run.
  - Right-click `src/Creational/FactoryMethod/Java/Example/Main.java` → Run.

- Terminal (Windows, from project root)
  - Structure
    ```bat
    javac -d out\factorymethod-structure src\Creational\FactoryMethod\Java\Structure\*.java
    java -cp out\factorymethod-structure Creational.FactoryMethod.Java.Structure.Main
    ```
  - Example
    ```bat
    javac -d out\factorymethod-example src\Creational\FactoryMethod\Java\Example\*.java
    java -cp out\factorymethod-example Creational.FactoryMethod.Java.Example.Main
    ```

Note: Ensure a JDK is installed and `javac`/`java` are available on PATH.

## Expected output (sample)

- Structure
  ```text
  ConcreteProduct1 operation
  ConcreteProduct2 operation
  ```

- Example
  ```text
  Deliver by land in a box
  Deliver by sea in a container
  ```

These outputs illustrate that the Creator delegates product creation to ConcreteCreators and executes behavior via a common interface.
