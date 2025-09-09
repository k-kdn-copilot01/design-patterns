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
        
        // Test Database Connection Singleton
        System.out.println("3. Testing Database Connection Singleton:");
        DatabaseConnection db1 = DatabaseConnection.getInstance();
        DatabaseConnection db2 = DatabaseConnection.getInstance();
        
        System.out.println("db1 == db2: " + (db1 == db2));
        System.out.println("Connection String: " + db1.getConnectionString());
        
        // Demonstrate database operations
        db1.connect();
        db1.executeQuery("SELECT * FROM users");
        db2.executeQuery("SELECT * FROM products"); // Same instance
        db1.disconnect();
        
        // Try to execute query after disconnect
        db2.executeQuery("SELECT * FROM orders");
        
        System.out.println("\n=== Demo Complete ===");
    }
}