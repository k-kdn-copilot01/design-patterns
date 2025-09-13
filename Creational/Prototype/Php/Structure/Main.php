<?php

// Include Prototype structure classes
require_once 'Prototype.php';
require_once 'ConcretePrototypeA.php';
require_once 'ConcretePrototypeB.php';
require_once 'Client.php';

/**
 * Main class to demonstrate Prototype structure implementations
 * 
 * This class shows how to use each type of Prototype pattern
 * and demonstrates that cloned objects are independent instances.
 */
class Main
{
    public static function run(): void
    {
        echo "=== Structure Demo: Prototype Pattern ===\n\n";
        
        // 1. Demonstrate Shallow Clone (ConcretePrototypeA)
        echo "1. Shallow Clone Demonstration:\n";
        $originalA = new ConcretePrototypeA("OriginalA", 100);
        echo "Original: " . $originalA->getInfo() . "\n";
        
        $cloneA = $originalA->clone();
        echo "Clone: " . $cloneA->getInfo() . "\n";
        
        // Check if they are different objects
        echo "originalA === cloneA: " . ($originalA === $cloneA ? 'true' : 'false') . "\n";
        
        // Modify data in original and see effect on clone (shallow copy behavior)
        $originalA->appendData("Modified by original");
        echo "After modifying original:\n";
        echo "Original: " . $originalA->getInfo() . "\n";
        echo "Clone: " . $cloneA->getInfo() . " (affected by shallow copy)\n";
        echo "\n";
        
        // 2. Demonstrate Deep Clone (ConcretePrototypeB)
        echo "2. Deep Clone Demonstration:\n";
        $originalB = new ConcretePrototypeB("OriginalB", 200);
        echo "Original: " . $originalB->getInfo() . "\n";
        
        $cloneB = $originalB->clone();
        echo "Clone: " . $cloneB->getInfo() . "\n";
        
        // Check if they are different objects
        echo "originalB === cloneB: " . ($originalB === $cloneB ? 'true' : 'false') . "\n";
        
        // Modify data in original and see effect on clone (deep copy behavior)
        $originalB->appendData("Modified by original");
        echo "After modifying original:\n";
        echo "Original: " . $originalB->getInfo() . "\n";
        echo "Clone: " . $cloneB->getInfo() . " (independent due to deep copy)\n";
        echo "\n";
        
        // 3. Demonstrate Client usage
        echo "3. Client Usage Demonstration:\n";
        $client = new Client($originalA);
        echo "Client prototype: " . $client->getPrototypeInfo() . "\n";
        
        $newObject1 = $client->createObject();
        $newObject2 = $client->createObject();
        
        echo "Created object 1: " . $newObject1->getInfo() . "\n";
        echo "Created object 2: " . $newObject2->getInfo() . "\n";
        echo "newObject1 === newObject2: " . ($newObject1 === $newObject2 ? 'true' : 'false') . "\n";
        
        // Change prototype and create more objects
        $client->setPrototype($originalB);
        $newObject3 = $client->createObject();
        echo "Created object 3 (from different prototype): " . $newObject3->getInfo() . "\n";
        
        echo "\n=== Structure Demo Complete ===\n";
    }
}

// Run the demo
Main::run();