package Creational.FactoryMethod.Java.Example;

public class RoadLogistics extends Logistics {
    @Override
    protected Transport createTransport() {
        return new Truck();
    }
}

