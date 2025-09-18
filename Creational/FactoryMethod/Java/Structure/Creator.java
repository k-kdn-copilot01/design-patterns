package Creational.FactoryMethod.Java.Structure;

public abstract class Creator {
    public abstract Product factoryMethod();

    public void doOperation() {
        Product p = factoryMethod();
        p.operation();
    }
}
