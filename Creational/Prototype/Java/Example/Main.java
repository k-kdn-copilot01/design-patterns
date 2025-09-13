public class Main {
    public static void main(String[] args) {
        System.out.println("=== Example Demo: Prototype Pattern Real-World Usage ===\n");
        
        // 1. Document Cloning Example
        System.out.println("1. Document Cloning Scenario:");
        Document originalDoc = new Document("Project Proposal", "This is the original content...", "John Doe");
        originalDoc.addTag("important");
        originalDoc.addTag("project");
        originalDoc.getMetadata().setStatus("Review");
        
        System.out.println("Original: " + originalDoc.getInfo());
        
        // Clone document for editing
        Document editedDoc = (Document) originalDoc.clone();
        editedDoc.setContent("This is the modified content...");
        editedDoc.addTag("modified");
        
        System.out.println("Edited Copy: " + editedDoc.getInfo());
        System.out.println("Original after cloning: " + originalDoc.getInfo());
        System.out.println("Independent copies: " + (originalDoc != editedDoc));
        System.out.println("Different versions: " + 
                         (originalDoc.getMetadata().getVersion() != editedDoc.getMetadata().getVersion()));
        System.out.println();
        
        // 2. Shape Cloning Example
        System.out.println("2. Shape Cloning Scenario:");
        
        // Create original shapes
        Circle originalCircle = new Circle(5.0, "red", 10, 20);
        Rectangle originalRectangle = new Rectangle(4.0, 6.0, "blue", 0, 0);
        
        System.out.println("Original Circle: " + originalCircle.getInfo());
        System.out.println("Original Rectangle: " + originalRectangle.getInfo());
        System.out.println();
        
        // Clone shapes and modify them
        Circle clonedCircle = (Circle) originalCircle.clone();
        clonedCircle.setRadius(8.0);
        clonedCircle.setColor("green");
        clonedCircle.setPosition(50, 60);
        
        Rectangle clonedRectangle = (Rectangle) originalRectangle.clone();
        clonedRectangle.setWidth(8.0);
        clonedRectangle.setHeight(3.0);
        clonedRectangle.setColor("yellow");
        clonedRectangle.setPosition(100, 200);
        
        System.out.println("After modifying clones:");
        System.out.println("Original Circle: " + originalCircle.getInfo());
        System.out.println("Cloned Circle: " + clonedCircle.getInfo());
        System.out.println("Original Rectangle: " + originalRectangle.getInfo());
        System.out.println("Cloned Rectangle: " + clonedRectangle.getInfo());
        System.out.println();
        
        // 3. Prototype Manager Example
        System.out.println("3. Prototype Manager Usage:");
        PrototypeManager manager = new PrototypeManager();
        
        // Register prototypes
        manager.registerPrototype("standard-circle", originalCircle);
        manager.registerPrototype("standard-rectangle", originalRectangle);
        manager.registerPrototype("template-document", originalDoc);
        
        // Create objects from prototypes
        Shape newCircle = (Shape) manager.createPrototype("standard-circle");
        Shape newRectangle = (Shape) manager.createPrototype("standard-rectangle");
        Document newDoc = (Document) manager.createPrototype("template-document");
        
        System.out.println("Created from prototypes:");
        System.out.println("New Circle: " + newCircle.getInfo());
        System.out.println("New Rectangle: " + newRectangle.getInfo());
        System.out.println("New Document: " + newDoc.getInfo());
        
        // Verify independence
        System.out.println("Objects are independent: " + 
                         (newCircle != originalCircle && newRectangle != originalRectangle && newDoc != originalDoc));
        
        System.out.println("\n=== Example Demo Complete ===");
    }
}