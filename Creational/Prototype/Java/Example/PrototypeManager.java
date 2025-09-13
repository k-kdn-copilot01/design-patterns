import java.util.HashMap;
import java.util.Map;

/**
 * PrototypeManager manages a registry of prototypes
 * and provides a way to create new objects by cloning registered prototypes
 */
public class PrototypeManager {
    private Map<String, Prototype> prototypes = new HashMap<>();
    
    /**
     * Register a prototype with a given name
     */
    public void registerPrototype(String name, Prototype prototype) {
        prototypes.put(name, prototype);
        System.out.println("Prototype registered: " + name);
    }
    
    /**
     * Create a new object by cloning the registered prototype
     */
    public Prototype createPrototype(String name) {
        Prototype prototype = prototypes.get(name);
        if (prototype != null) {
            return prototype.clone();
        }
        throw new IllegalArgumentException("Prototype not found: " + name);
    }
    
    /**
     * Remove a prototype from the registry
     */
    public void unregisterPrototype(String name) {
        prototypes.remove(name);
        System.out.println("Prototype unregistered: " + name);
    }
    
    /**
     * Get list of registered prototype names
     */
    public String[] getRegisteredNames() {
        return prototypes.keySet().toArray(new String[0]);
    }
}