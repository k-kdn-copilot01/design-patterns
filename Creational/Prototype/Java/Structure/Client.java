/**
 * Client Class
 * 
 * This class demonstrates how to use prototypes for object creation.
 * It shows how cloning can be more efficient than creating new objects
 * when the initialization is complex or expensive.
 */
public class Client {
    private Prototype prototype;
    
    public Client(Prototype prototype) {
        this.prototype = prototype;
    }
    
    /**
     * Creates a new object by cloning the stored prototype
     */
    public Prototype createObject() {
        return prototype.clone();
    }
    
    /**
     * Changes the prototype to a different one
     */
    public void setPrototype(Prototype prototype) {
        this.prototype = prototype;
    }
    
    /**
     * Gets information about the current prototype
     */
    public String getPrototypeInfo() {
        return prototype.getInfo();
    }
}