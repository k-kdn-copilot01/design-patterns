/**
 * Prototype Interface
 * 
 * This interface defines the contract for objects that can be cloned.
 * The clone() method should create a copy of the current object.
 */
public interface Prototype {
    /**
     * Creates a copy of the current object
     * 
     * @return A new instance that is a copy of the current object
     */
    Prototype clone();
    
    /**
     * Returns a string representation of the object for demonstration purposes
     */
    String getInfo();
}