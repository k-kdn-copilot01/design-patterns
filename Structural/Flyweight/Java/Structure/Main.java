/**
 * Flyweight Interface
 * 
 * This interface defines the common operations that all flyweight objects must implement.
 */
interface Flyweight {
    void operation(String extrinsicState);
}

/**
 * Concrete Flyweight Implementation
 * 
 * This represents a concrete flyweight object that stores intrinsic state
 * and can be shared across multiple contexts.
 */
class ConcreteFlyweight implements Flyweight {
    private String intrinsicState;
    
    public ConcreteFlyweight(String intrinsicState) {
        this.intrinsicState = intrinsicState;
        System.out.println("ConcreteFlyweight created with intrinsic state: " + intrinsicState);
    }
    
    @Override
    public void operation(String extrinsicState) {
        System.out.println("ConcreteFlyweight: Operation with extrinsic state: " + extrinsicState);
    }
    
    public String getIntrinsicState() {
        return intrinsicState;
    }
}

/**
 * Flyweight Factory
 * 
 * This factory manages the creation and caching of flyweight objects.
 * It ensures that flyweights with the same intrinsic state are reused.
 */
class FlyweightFactory {
    private java.util.Map<String, Flyweight> flyweights = new java.util.HashMap<>();
    
    public Flyweight getFlyweight(String key) {
        if (flyweights.containsKey(key)) {
            System.out.println("FlyweightFactory: Reusing existing ConcreteFlyweight with key: " + key);
            return flyweights.get(key);
        } else {
            System.out.println("FlyweightFactory: Creating new ConcreteFlyweight with key: " + key);
            ConcreteFlyweight flyweight = new ConcreteFlyweight(key);
            flyweights.put(key, flyweight);
            return flyweight;
        }
    }
    
    public int getFlyweightCount() {
        return flyweights.size();
    }
}

/**
 * Client Class
 * 
 * This class demonstrates how to use flyweights with extrinsic state.
 */
class Client {
    private FlyweightFactory factory;
    
    public Client() {
        this.factory = new FlyweightFactory();
    }
    
    public void useFlyweight(String intrinsicState, String extrinsicState) {
        Flyweight flyweight = factory.getFlyweight(intrinsicState);
        flyweight.operation(extrinsicState);
    }
    
    public int getFlyweightCount() {
        return factory.getFlyweightCount();
    }
}

/**
 * Main class to demonstrate Flyweight pattern implementations
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Structure Demo: Flyweight Implementations ===\n");
        
        // Basic Flyweight
        System.out.println("1. Basic Flyweight:");
        Client client = new Client();
        client.useFlyweight("A", "State1");
        client.useFlyweight("A", "State2"); // Reuses existing flyweight
        System.out.println();
        
        // Multiple Flyweights
        System.out.println("2. Multiple Flyweights:");
        client.useFlyweight("B", "State3");
        
        System.out.println("\nTotal flyweights created: " + client.getFlyweightCount());
        System.out.println("\n=== Structure Demo Complete ===");
    }
}
