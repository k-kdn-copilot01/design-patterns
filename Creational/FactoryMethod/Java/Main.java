/**
 * Main Class - Factory Method Pattern Demo
 * 
 * Demonstrates the Factory Method pattern by showing how different
 * ConcreteCreators can create different ConcreteProducts while using
 * the same interface and business logic.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Factory Method Design Pattern Demo ===\n");
        
        // Demonstrate polymorphism: same interface, different implementations
        System.out.println("1. Testing Road Logistics:");
        Logistics roadLogistics = new RoadLogistics();
        roadLogistics.planDelivery();
        
        System.out.println("2. Testing Sea Logistics:");
        Logistics seaLogistics = new SeaLogistics();
        seaLogistics.planDelivery();
        
        // Demonstrate that different creators produce different products
        System.out.println("3. Comparing Transport Types:");
        Transport truck = roadLogistics.createTransport();
        Transport ship = seaLogistics.createTransport();
        
        System.out.println("Road transport: " + truck.getTransportType() + " (Cost: $" + truck.getCost() + ")");
        System.out.println("Sea transport: " + ship.getTransportType() + " (Cost: $" + ship.getCost() + ")");
        System.out.println("Are they the same type? " + (truck.getClass() == ship.getClass()));
        System.out.println();
        
        // Demonstrate business logic reuse with different products
        System.out.println("4. Demonstrating Polymorphism:");
        performDelivery(roadLogistics);
        performDelivery(seaLogistics);
        
        System.out.println("=== Demo Complete ===");
    }
    
    /**
     * Utility method để demonstarte polymorphism
     * Method này không cần biết concrete type của logistics
     */
    private static void performDelivery(Logistics logistics) {
        System.out.println("Performing delivery with: " + logistics.getLogisticsType());
        Transport transport = logistics.createTransport();
        transport.deliver();
        System.out.println();
    }
}