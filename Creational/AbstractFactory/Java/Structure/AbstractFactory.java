/**
 * Abstract Factory interface that declares methods for creating
 * a family of related products (ProductA and ProductB).
 */
public interface AbstractFactory {
    ProductA createProductA();
    ProductB createProductB();
}