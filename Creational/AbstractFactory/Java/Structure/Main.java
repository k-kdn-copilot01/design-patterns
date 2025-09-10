/**
 * Main class demonstrating Abstract Factory pattern structure
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Structure Demo: Abstract Factory Pattern ===\n");
        
        // Create client with Factory 1
        System.out.println("1. Using ConcreteFactory1:");
        AbstractFactory factory1 = new ConcreteFactory1();
        Client client1 = new Client(factory1);
        client1.run();
        
        // Create client with Factory 2 
        System.out.println("2. Using ConcreteFactory2:");
        AbstractFactory factory2 = new ConcreteFactory2();
        Client client2 = new Client(factory2);
        client2.run();
        
        System.out.println("=== Structure Demo Complete ===");
    }
}