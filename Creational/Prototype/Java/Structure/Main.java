public class Main {
    public static void main(String[] args) {
        System.out.println("=== Structure Demo: Prototype Pattern ===\n");
        
        // 1. Demonstrate Shallow Clone (ConcretePrototypeA)
        System.out.println("1. Shallow Clone Demonstration:");
        ConcretePrototypeA originalA = new ConcretePrototypeA("OriginalA", 100);
        System.out.println("Original: " + originalA.getInfo());
        
        ConcretePrototypeA cloneA = (ConcretePrototypeA) originalA.clone();
        System.out.println("Clone: " + cloneA.getInfo());
        
        // Check if they are different objects
        System.out.println("originalA == cloneA: " + (originalA == cloneA));
        System.out.println("originalA.equals(cloneA): " + originalA.equals(cloneA));
        
        // Modify data in original and see effect on clone (shallow copy behavior)
        originalA.appendData("Modified by original");
        System.out.println("After modifying original:");
        System.out.println("Original: " + originalA.getInfo());
        System.out.println("Clone: " + cloneA.getInfo() + " (affected by shallow copy)");
        System.out.println();
        
        // 2. Demonstrate Deep Clone (ConcretePrototypeB)
        System.out.println("2. Deep Clone Demonstration:");
        ConcretePrototypeB originalB = new ConcretePrototypeB("OriginalB", 200);
        System.out.println("Original: " + originalB.getInfo());
        
        ConcretePrototypeB cloneB = (ConcretePrototypeB) originalB.clone();
        System.out.println("Clone: " + cloneB.getInfo());
        
        // Check if they are different objects
        System.out.println("originalB == cloneB: " + (originalB == cloneB));
        
        // Modify data in original and see effect on clone (deep copy behavior)
        originalB.appendData("Modified by original");
        System.out.println("After modifying original:");
        System.out.println("Original: " + originalB.getInfo());
        System.out.println("Clone: " + cloneB.getInfo() + " (independent due to deep copy)");
        System.out.println();
        
        // 3. Demonstrate Client usage
        System.out.println("3. Client Usage Demonstration:");
        Client client = new Client(originalA);
        System.out.println("Client prototype: " + client.getPrototypeInfo());
        
        Prototype newObject1 = client.createObject();
        Prototype newObject2 = client.createObject();
        
        System.out.println("Created object 1: " + newObject1.getInfo());
        System.out.println("Created object 2: " + newObject2.getInfo());
        System.out.println("newObject1 == newObject2: " + (newObject1 == newObject2));
        
        // Change prototype and create more objects
        client.setPrototype(originalB);
        Prototype newObject3 = client.createObject();
        System.out.println("Created object 3 (from different prototype): " + newObject3.getInfo());
        
        System.out.println("\n=== Structure Demo Complete ===");
    }
}