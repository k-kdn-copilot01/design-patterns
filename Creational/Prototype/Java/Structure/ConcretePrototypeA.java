/**
 * Concrete Prototype A Implementation
 * 
 * This concrete prototype maintains its own state and can create clones of itself.
 * Demonstrates basic prototype cloning functionality.
 */
public class ConcretePrototypeA implements Prototype {
    private String data;
    private int value;
    
    public ConcretePrototypeA(String data, int value) {
        this.data = data;
        this.value = value;
        System.out.println("ConcretePrototypeA created with data: " + data + ", value: " + value);
    }
    
    // Copy constructor for cloning
    private ConcretePrototypeA(ConcretePrototypeA original) {
        this.data = original.data;
        this.value = original.value;
        System.out.println("ConcretePrototypeA cloned with data: " + data + ", value: " + value);
    }
    
    @Override
    public Prototype clone() {
        return new ConcretePrototypeA(this);
    }
    
    @Override
    public void display() {
        System.out.println("ConcretePrototypeA [data=" + data + ", value=" + value + "]");
    }
    
    // Getters for demonstration purposes
    public String getData() {
        return data;
    }
    
    public int getValue() {
        return value;
    }
    
    // Setter to demonstrate independence of clones
    public void setData(String data) {
        this.data = data;
    }
    
    public void setValue(int value) {
        this.value = value;
    }
}