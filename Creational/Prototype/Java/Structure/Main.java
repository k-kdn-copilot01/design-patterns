/**
 * Main class to demonstrate Prototype structure implementations
 * 
 * This class shows how to use the Prototype pattern to clone objects
 * and demonstrates that cloned objects are independent instances.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Structure Demo: Prototype Pattern ===\n");
        
        // Create original prototypes
        System.out.println("1. Creating original prototypes:");
        ConcretePrototypeA prototypeA = new ConcretePrototypeA("Original Data", 42);
        ConcretePrototypeB prototypeB = new ConcretePrototypeB("Original Name", true);
        System.out.println();
        
        // Test cloning with ConcretePrototypeA
        System.out.println("2. Cloning ConcretePrototypeA:");
        Prototype cloneA1 = prototypeA.clone();
        Prototype cloneA2 = prototypeA.clone();
        
        // Verify they are different instances but same content
        System.out.println("Original == Clone1: " + (prototypeA == cloneA1));
        System.out.println("Clone1 == Clone2: " + (cloneA1 == cloneA2));
        
        System.out.println("\nOriginal and clones display:");
        prototypeA.display();
        cloneA1.display();
        cloneA2.display();
        System.out.println();
        
        // Demonstrate independence by modifying clone
        System.out.println("3. Modifying clone to show independence:");
        ((ConcretePrototypeA) cloneA1).setData("Modified Data");
        ((ConcretePrototypeA) cloneA1).setValue(99);
        
        System.out.println("After modifying clone1:");
        System.out.print("Original: ");
        prototypeA.display();
        System.out.print("Clone1: ");
        cloneA1.display();
        System.out.print("Clone2: ");
        cloneA2.display();
        System.out.println();
        
        // Test with Client class
        System.out.println("4. Using Client class:");
        Client client = new Client(prototypeB);
        client.displayPrototype();
        
        Prototype cloneB = client.createClone();
        System.out.print("Cloned via Client: ");
        cloneB.display();
        
        // Verify independence
        System.out.println("Original == Clone: " + (prototypeB == cloneB));
        
        // Change prototype in client
        client.setPrototype(prototypeA);
        System.out.println("\nChanged client prototype:");
        client.displayPrototype();
        Prototype newClone = client.createClone();
        System.out.print("New clone: ");
        newClone.display();
        
        System.out.println("\n=== Structure Demo Complete ===");
    }
}