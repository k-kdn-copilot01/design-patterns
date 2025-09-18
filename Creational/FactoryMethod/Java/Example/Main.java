package Creational.FactoryMethod.Java.Example;

public class Main {
    public static void main(String[] args) {
        Logistics road = new RoadLogistics();
        Logistics sea = new SeaLogistics();

        road.planDelivery();
        sea.planDelivery();
    }
}

