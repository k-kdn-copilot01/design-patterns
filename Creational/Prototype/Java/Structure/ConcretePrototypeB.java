/**
 * Concrete Prototype B Implementation
 * 
 * This concrete prototype demonstrates a different type of object that can be cloned.
 * Shows how different classes can implement the same prototype interface.
 */
public class ConcretePrototypeB implements Prototype {
    private String name;
    private boolean active;
    
    public ConcretePrototypeB(String name, boolean active) {
        this.name = name;
        this.active = active;
        System.out.println("ConcretePrototypeB created with name: " + name + ", active: " + active);
    }
    
    // Copy constructor for cloning
    private ConcretePrototypeB(ConcretePrototypeB original) {
        this.name = original.name;
        this.active = original.active;
        System.out.println("ConcretePrototypeB cloned with name: " + name + ", active: " + active);
    }
    
    @Override
    public Prototype clone() {
        return new ConcretePrototypeB(this);
    }
    
    @Override
    public void display() {
        System.out.println("ConcretePrototypeB [name=" + name + ", active=" + active + "]");
    }
    
    // Getters for demonstration purposes
    public String getName() {
        return name;
    }
    
    public boolean isActive() {
        return active;
    }
    
    // Setters to demonstrate independence of clones
    public void setName(String name) {
        this.name = name;
    }
    
    public void setActive(boolean active) {
        this.active = active;
    }
}