/**
 * ConcretePrototypeA Implementation
 * 
 * This class implements shallow cloning. All primitive fields are copied,
 * but object references are shared between the original and clone.
 */
public class ConcretePrototypeA implements Prototype {
    private String name;
    private int value;
    private StringBuilder data; // This will be shared in shallow clone
    
    public ConcretePrototypeA(String name, int value) {
        this.name = name;
        this.value = value;
        this.data = new StringBuilder("Initial data for " + name);
        System.out.println("ConcretePrototypeA created: " + name);
    }
    
    // Private constructor for cloning
    private ConcretePrototypeA(ConcretePrototypeA other) {
        this.name = other.name + " (Clone)";
        this.value = other.value;
        this.data = other.data; // Shallow copy - same reference
        System.out.println("ConcretePrototypeA cloned: " + this.name);
    }
    
    @Override
    public Prototype clone() {
        return new ConcretePrototypeA(this);
    }
    
    @Override
    public String getInfo() {
        return String.format("ConcretePrototypeA[name=%s, value=%d, data=%s]", 
                           name, value, data.toString());
    }
    
    public void appendData(String newData) {
        data.append(" - ").append(newData);
    }
    
    public String getName() {
        return name;
    }
    
    public int getValue() {
        return value;
    }
}