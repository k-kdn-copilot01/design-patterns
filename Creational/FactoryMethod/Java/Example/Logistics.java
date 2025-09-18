package Creational.FactoryMethod.Java.Example;

public abstract class Logistics {
    protected abstract Transport createTransport();

    public void planDelivery() {
        Transport t = createTransport();
        t.deliver();
    }
}

