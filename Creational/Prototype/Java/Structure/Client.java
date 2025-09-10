/**
 * Client Class
 * 
 * The client works with prototypes through the Prototype interface.
 * It can clone objects without knowing their concrete types.
 */
public class Client {
    private Prototype prototype;
    
    public Client(Prototype prototype) {
        this.prototype = prototype;
    }
    
    /**
     * Creates a clone of the stored prototype
     * @return A clone of the prototype
     */
    public Prototype createClone() {
        return prototype.clone();
    }
    
    /**
     * Sets a new prototype to be cloned
     * @param prototype The new prototype to store
     */
    public void setPrototype(Prototype prototype) {
        this.prototype = prototype;
    }
    
    /**
     * Displays the current prototype
     */
    public void displayPrototype() {
        System.out.print("Current prototype: ");
        prototype.display();
    }
}