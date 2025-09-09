/**
 * Lazy Singleton Implementation
 * 
 * This implementation creates the instance only when it's first needed.
 * Warning: This is NOT thread-safe and should only be used in single-threaded environments.
 */
public class LazySingleton {
    private static LazySingleton instance;
    
    // Private constructor to prevent external instantiation
    private LazySingleton() {
        System.out.println("LazySingleton instance created");
    }
    
    // Public method to get the instance (lazy initialization)
    public static LazySingleton getInstance() {
        if (instance == null) {
            instance = new LazySingleton();
        }
        return instance;
    }
    
    // Example method to demonstrate functionality
    public void doSomething() {
        System.out.println("LazySingleton is doing something...");
    }
}