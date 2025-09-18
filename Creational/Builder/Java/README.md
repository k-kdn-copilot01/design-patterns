# Builder Pattern - Java

A creational pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

## Directory structure

```
src/
└── Creational/                       
    └── Builder/
        └── Java/
            ├── Example/          
            │   ├── Main.java
            │   └── Product.java
            └── Structure/
                ├── Main.java   
                └── SampleObject.java
```

## How to run

- IntelliJ IDEA
  - Open the project.
  - Right-click `src/Creational/Builder/Java/Example/Main.java` → Run.
  - Right-click `src/Creational/Builder/Java/Structure/Main.java` → Run.

- Terminal (Windows, run from project root)
  - Example
    ```bat
    javac -d out\builder-example src\Creational\Builder\Java\Example\*.java
    java -cp out\builder-example Creational.Builder.Java.Example.Main
    ```
  - Structure
    ```bat
    javac -d out\builder-structure src\Creational\Builder\Java\Structure\*.java
    java -cp out\builder-structure Creational.Builder.Java.Structure.Main
    ```

Note: Ensure a JDK is installed and `javac`/`java` are available on PATH.

## Expected output (sample)

- Example
  ```text
  Product ID: P001
  Product Name: Laptop
  Product Price: $999.99
  Product ID: P002
  Product Name: Smartphone
  Product Price: $0.0
  ```

- Structure
  ```text
  value1 value2 null
  ```

These samples illustrate typical output when constructing objects via the Builder; your exact values may differ based on the code in `Main.java`.