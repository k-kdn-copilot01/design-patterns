<?php

// Include example classes
require_once 'Shape.php';
require_once 'Circle.php';
require_once 'Rectangle.php';

/**
 * Main class to demonstrate Prototype pattern with real-world example
 * 
 * This class shows how the Prototype pattern can be used to efficiently
 * create multiple variations of geometric shapes without knowing their concrete types.
 */
class Main
{
    public static function run(): void
    {
        echo "=== Prototype Design Pattern Demo ===\n\n";
        
        // Create original shape prototypes
        echo "1. Creating original shape prototypes:\n";
        $circlePrototype = new Circle("Red", 10, 20, 15);
        $rectanglePrototype = new Rectangle("Blue", 30, 40, 25, 35);
        echo "\n";
        
        // Clone shapes to create variations
        echo "2. Cloning shapes to create variations:\n";
        $shapes = [];
        
        // Clone circles with different positions/properties
        echo "Cloning circle...\n";
        $circle1 = $circlePrototype->clone();
        $circle1->setColor("Green");
        $circle1->move(50, 60);
        $shapes[] = $circle1;
        
        echo "Cloning circle...\n";
        $circle2 = $circlePrototype->clone();
        $circle2->setRadius(20);
        $circle2->move(80, 90);
        $shapes[] = $circle2;
        
        // Clone rectangles with different properties
        echo "Cloning rectangle...\n";
        $rectangle1 = $rectanglePrototype->clone();
        $rectangle1->setColor("Yellow");
        $rectangle1->move(100, 110);
        $shapes[] = $rectangle1;
        
        echo "Cloning rectangle...\n";
        $rectangle2 = $rectanglePrototype->clone();
        $rectangle2->setWidth(40);
        $rectangle2->setHeight(50);
        $rectangle2->move(120, 130);
        $shapes[] = $rectangle2;
        
        echo "\n";
        
        // Display all shapes
        echo "3. Drawing all shapes:\n";
        echo "Original prototypes:\n";
        $circlePrototype->draw();
        $rectanglePrototype->draw();
        
        echo "\nCloned variations:\n";
        foreach ($shapes as $shape) {
            $shape->draw();
        }
        echo "\n";
        
        // Demonstrate object independence
        echo "4. Demonstrating object independence:\n";
        echo "Original circle area: " . number_format($circlePrototype->getArea(), 2) . "\n";
        echo "Cloned circle area: " . number_format($circle1->getArea(), 2) . "\n";
        echo "Modified circle area: " . number_format($circle2->getArea(), 2) . "\n";
        
        echo "\nReference comparison:\n";
        echo "Original === Clone1: " . ($circlePrototype === $circle1 ? 'true' : 'false') . "\n";
        echo "Clone1 === Clone2: " . ($circle1 === $circle2 ? 'true' : 'false') . "\n";
        echo "\n";
        
        // Demonstrate efficiency of cloning vs creating new
        echo "5. Performance comparison (cloning vs new creation):\n";
        
        // Enable silent mode for performance testing
        Circle::setSilentMode(true);
        
        // Time cloning (silent)
        $startTime = microtime(true);
        for ($i = 0; $i < 1000; $i++) {
            $clonedShape = $circlePrototype->clone();
        }
        $endTime = microtime(true);
        $cloneTime = $endTime - $startTime;
        
        // Time new creation (silent)
        $startTime = microtime(true);
        for ($i = 0; $i < 1000; $i++) {
            $newShape = new Circle();
            $newShape->setColor("Red");
            $newShape->setX(10);
            $newShape->setY(20);
            $newShape->setRadius(15);
        }
        $endTime = microtime(true);
        $newTime = $endTime - $startTime;
        
        // Disable silent mode
        Circle::setSilentMode(false);
        
        echo "Time for 1000 clones: " . number_format($cloneTime * 1000000) . " microseconds\n";
        echo "Time for 1000 new objects: " . number_format($newTime * 1000000) . " microseconds\n";
        echo "Cloning is " . number_format($newTime / $cloneTime, 2) . "x faster\n";
        
        echo "\n=== Demo Complete ===\n";
    }
}

// Run the demo
Main::run();