/**
 * Main class to demonstrate all Singleton implementations
 * 
 * This class shows how to use each type of Singleton pattern
 * and demonstrates that only one instance is created for each type.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Singleton Design Pattern Demo ===\n");
        
        // Test Lazy Singleton
        System.out.println("1. Testing Lazy Singleton:");
        LazySingleton lazy1 = LazySingleton.getInstance();
        LazySingleton lazy2 = LazySingleton.getInstance();
        
        System.out.println("lazy1 == lazy2: " + (lazy1 == lazy2));
        lazy1.doSomething();
        System.out.println();
        
        // Test Eager Singleton
        System.out.println("2. Testing Eager Singleton:");
        EagerSingleton eager1 = EagerSingleton.getInstance();
        EagerSingleton eager2 = EagerSingleton.getInstance();
        
        System.out.println("eager1 == eager2: " + (eager1 == eager2));
        eager1.doSomething();
        System.out.println();
        
        System.out.println("\n=== Demo Complete ===");
    }
}