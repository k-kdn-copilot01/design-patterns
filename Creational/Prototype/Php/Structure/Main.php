<?php

// Include Prototype structure classes
require_once 'Prototype.php';
require_once 'ConcretePrototypeA.php';
require_once 'ConcretePrototypeB.php';
require_once 'Client.php';

/**
 * Main class to demonstrate Prototype structure implementations
 * 
 * This class shows how to use the Prototype pattern to clone objects
 * and demonstrates that cloned objects are independent instances.
 */
class Main
{
    public static function run(): void
    {
        echo "=== Structure Demo: Prototype Pattern ===\n\n";
        
        // Create original prototypes
        echo "1. Creating original prototypes:\n";
        $prototypeA = new ConcretePrototypeA("Original Data", 42);
        $prototypeB = new ConcretePrototypeB("Original Name", true);
        echo "\n";
        
        // Test cloning with ConcretePrototypeA
        echo "2. Cloning ConcretePrototypeA:\n";
        $cloneA1 = $prototypeA->clone();
        $cloneA2 = $prototypeA->clone();
        
        // Verify they are different instances but same content
        echo "Original === Clone1: " . ($prototypeA === $cloneA1 ? 'true' : 'false') . "\n";
        echo "Clone1 === Clone2: " . ($cloneA1 === $cloneA2 ? 'true' : 'false') . "\n";
        
        echo "\nOriginal and clones display:\n";
        $prototypeA->display();
        $cloneA1->display();
        $cloneA2->display();
        echo "\n";
        
        // Demonstrate independence by modifying clone
        echo "3. Modifying clone to show independence:\n";
        $cloneA1->setData("Modified Data");
        $cloneA1->setValue(99);
        
        echo "After modifying clone1:\n";
        echo "Original: ";
        $prototypeA->display();
        echo "Clone1: ";
        $cloneA1->display();
        echo "Clone2: ";
        $cloneA2->display();
        echo "\n";
        
        // Test with Client class
        echo "4. Using Client class:\n";
        $client = new Client($prototypeB);
        $client->displayPrototype();
        
        $cloneB = $client->createClone();
        echo "Cloned via Client: ";
        $cloneB->display();
        
        // Verify independence
        echo "Original === Clone: " . ($prototypeB === $cloneB ? 'true' : 'false') . "\n";
        
        // Change prototype in client
        $client->setPrototype($prototypeA);
        echo "\nChanged client prototype:\n";
        $client->displayPrototype();
        $newClone = $client->createClone();
        echo "New clone: ";
        $newClone->display();
        
        echo "\n=== Structure Demo Complete ===\n";
    }
}

// Run the demo
Main::run();