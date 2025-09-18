package Creational.FactoryMethod.Java.Structure;

public class Main {
    public static void main(String[] args) {
        Creator c1 = new ConcreteCreator1();
        Creator c2 = new ConcreteCreator2();

        Client.run(c1);
        Client.run(c2);
    }
}
