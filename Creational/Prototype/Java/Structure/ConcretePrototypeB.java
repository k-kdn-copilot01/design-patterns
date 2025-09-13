/**
 * ConcretePrototypeB Implementation
 * 
 * This class implements deep cloning. All fields, including object references,
 * are copied to create completely independent objects.
 */
public class ConcretePrototypeB implements Prototype {
    private String name;
    private int value;
    private StringBuilder data; // This will be deeply copied
    
    public ConcretePrototypeB(String name, int value) {
        this.name = name;
        this.value = value;
        this.data = new StringBuilder("Initial data for " + name);
        System.out.println("ConcretePrototypeB created: " + name);
    }
    
    // Private constructor for cloning
    private ConcretePrototypeB(ConcretePrototypeB other) {
        this.name = other.name + " (Deep Clone)";
        this.value = other.value;
        this.data = new StringBuilder(other.data.toString()); // Deep copy - new instance
        System.out.println("ConcretePrototypeB deep cloned: " + this.name);
    }
    
    @Override
    public Prototype clone() {
        return new ConcretePrototypeB(this);
    }
    
    @Override
    public String getInfo() {
        return String.format("ConcretePrototypeB[name=%s, value=%d, data=%s]", 
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