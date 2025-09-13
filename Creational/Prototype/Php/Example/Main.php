<?php

// Include example classes
require_once 'Prototype.php';
require_once 'Document.php';
require_once 'DocumentMetadata.php';
require_once 'Shape.php';
require_once 'Circle.php';
require_once 'Rectangle.php';
require_once 'PrototypeManager.php';

/**
 * Main class to demonstrate Prototype design pattern with real-world examples
 * 
 * This class shows how to use the Prototype pattern with practical scenarios
 * and demonstrates that cloned objects are independent instances.
 */
class Main
{
    public static function run(): void
    {
        echo "=== Example Demo: Prototype Pattern Real-World Usage ===\n\n";
        
        // 1. Document Cloning Example
        echo "1. Document Cloning Scenario:\n";
        $originalDoc = new Document("Project Proposal", "This is the original content...", "John Doe");
        $originalDoc->addTag("important");
        $originalDoc->addTag("project");
        $originalDoc->getMetadata()->setStatus("Review");
        
        echo "Original: " . $originalDoc->getInfo() . "\n";
        
        // Clone document for editing
        $editedDoc = $originalDoc->clone();
        $editedDoc->setContent("This is the modified content...");
        $editedDoc->addTag("modified");
        
        echo "Edited Copy: " . $editedDoc->getInfo() . "\n";
        echo "Original after cloning: " . $originalDoc->getInfo() . "\n";
        echo "Independent copies: " . ($originalDoc !== $editedDoc ? 'true' : 'false') . "\n";
        echo "Different versions: " . 
             ($originalDoc->getMetadata()->getVersion() !== $editedDoc->getMetadata()->getVersion() ? 'true' : 'false') . "\n";
        echo "\n";
        
        // 2. Shape Cloning Example
        echo "2. Shape Cloning Scenario:\n";
        
        // Create original shapes
        $originalCircle = new Circle(5.0, "red", 10, 20);
        $originalRectangle = new Rectangle(4.0, 6.0, "blue", 0, 0);
        
        echo "Original Circle: " . $originalCircle->getInfo() . "\n";
        echo "Original Rectangle: " . $originalRectangle->getInfo() . "\n";
        echo "\n";
        
        // Clone shapes and modify them
        $clonedCircle = $originalCircle->clone();
        $clonedCircle->setRadius(8.0);
        $clonedCircle->setColor("green");
        $clonedCircle->setPosition(50, 60);
        
        $clonedRectangle = $originalRectangle->clone();
        $clonedRectangle->setWidth(8.0);
        $clonedRectangle->setHeight(3.0);
        $clonedRectangle->setColor("yellow");
        $clonedRectangle->setPosition(100, 200);
        
        echo "After modifying clones:\n";
        echo "Original Circle: " . $originalCircle->getInfo() . "\n";
        echo "Cloned Circle: " . $clonedCircle->getInfo() . "\n";
        echo "Original Rectangle: " . $originalRectangle->getInfo() . "\n";
        echo "Cloned Rectangle: " . $clonedRectangle->getInfo() . "\n";
        echo "\n";
        
        // 3. Prototype Manager Example
        echo "3. Prototype Manager Usage:\n";
        $manager = new PrototypeManager();
        
        // Register prototypes
        $manager->registerPrototype("standard-circle", $originalCircle);
        $manager->registerPrototype("standard-rectangle", $originalRectangle);
        $manager->registerPrototype("template-document", $originalDoc);
        
        // Create objects from prototypes
        $newCircle = $manager->createPrototype("standard-circle");
        $newRectangle = $manager->createPrototype("standard-rectangle");
        $newDoc = $manager->createPrototype("template-document");
        
        echo "Created from prototypes:\n";
        echo "New Circle: " . $newCircle->getInfo() . "\n";
        echo "New Rectangle: " . $newRectangle->getInfo() . "\n";
        echo "New Document: " . $newDoc->getInfo() . "\n";
        
        // Verify independence
        echo "Objects are independent: " . 
             ($newCircle !== $originalCircle && $newRectangle !== $originalRectangle && $newDoc !== $originalDoc ? 'true' : 'false') . "\n";
        
        echo "\n=== Example Demo Complete ===\n";
    }
}

// Run the demo
Main::run();