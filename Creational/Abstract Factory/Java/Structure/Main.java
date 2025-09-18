public class Main {
    public static void main(String[] args) {
        System.out.println("--- Abstract Factory: Structure demo ---");

        System.out.println("Using ConcreteFactory1 (family 1):");
        AbstractFactory factory1 = new ConcreteFactory1();
        Client client1 = new Client(factory1);
        client1.run();

        System.out.println("\nUsing ConcreteFactory2 (family 2):");
        AbstractFactory factory2 = new ConcreteFactory2();
        Client client2 = new Client(factory2);
        client2.run();
    }
}
