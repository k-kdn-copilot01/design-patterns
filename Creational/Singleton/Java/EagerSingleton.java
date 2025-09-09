/**
 * Eager Singleton Implementation
 * 
 * This implementation creates the instance at class loading time.
 * This is thread-safe because class loading is handled by the JVM.
 */
public class EagerSingleton {
    // Instance is created at class loading time (eager initialization)
    private static final EagerSingleton instance = new EagerSingleton();
    
    // Private constructor to prevent external instantiation
    private EagerSingleton() {
        System.out.println("EagerSingleton instance created");
    }
    
    // Public method to get the instance
    public static EagerSingleton getInstance() {
        return instance;
    }
    
    // Example method to demonstrate functionality
    public void doSomething() {
        System.out.println("EagerSingleton is doing something...");
    }
}