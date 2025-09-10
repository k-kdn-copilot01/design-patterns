/**
 * Prototype Interface
 * 
 * Declares the clone method that concrete prototypes must implement.
 * This interface enables objects to be cloned without knowing their concrete types.
 */
public interface Prototype {
    /**
     * Creates and returns a copy of this object
     * @return A clone of this prototype
     */
    Prototype clone();
    
    /**
     * Display information about this prototype
     */
    void display();
}