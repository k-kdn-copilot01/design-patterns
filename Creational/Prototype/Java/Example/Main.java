import java.util.ArrayList;
import java.util.List;

/**
 * Main class to demonstrate Prototype pattern with real-world example
 * 
 * This class shows how the Prototype pattern can be used to efficiently
 * create multiple variations of geometric shapes without knowing their concrete types.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Prototype Design Pattern Demo ===\n");
        
        // Create original shape prototypes
        System.out.println("1. Creating original shape prototypes:");
        Circle circlePrototype = new Circle("Red", 10, 20, 15);
        Rectangle rectanglePrototype = new Rectangle("Blue", 30, 40, 25, 35);
        System.out.println();
        
        // Clone shapes to create variations
        System.out.println("2. Cloning shapes to create variations:");
        List<Shape> shapes = new ArrayList<>();
        
        // Clone circles with different positions/properties
        System.out.println("Cloning circle...");
        Shape circle1 = circlePrototype.clone();
        circle1.setColor("Green");
        circle1.move(50, 60);
        shapes.add(circle1);
        
        System.out.println("Cloning circle...");
        Shape circle2 = circlePrototype.clone();
        ((Circle) circle2).setRadius(20);
        circle2.move(80, 90);
        shapes.add(circle2);
        
        // Clone rectangles with different properties
        System.out.println("Cloning rectangle...");
        Shape rectangle1 = rectanglePrototype.clone();
        rectangle1.setColor("Yellow");
        rectangle1.move(100, 110);
        shapes.add(rectangle1);
        
        System.out.println("Cloning rectangle...");
        Shape rectangle2 = rectanglePrototype.clone();
        ((Rectangle) rectangle2).setWidth(40);
        ((Rectangle) rectangle2).setHeight(50);
        rectangle2.move(120, 130);
        shapes.add(rectangle2);
        
        System.out.println();
        
        // Display all shapes
        System.out.println("3. Drawing all shapes:");
        System.out.println("Original prototypes:");
        circlePrototype.draw();
        rectanglePrototype.draw();
        
        System.out.println("\nCloned variations:");
        for (Shape shape : shapes) {
            shape.draw();
        }
        System.out.println();
        
        // Demonstrate object independence
        System.out.println("4. Demonstrating object independence:");
        System.out.println("Original circle area: " + String.format("%.2f", circlePrototype.getArea()));
        System.out.println("Cloned circle area: " + String.format("%.2f", circle1.getArea()));
        System.out.println("Modified circle area: " + String.format("%.2f", circle2.getArea()));
        
        System.out.println("\nReference comparison:");
        System.out.println("Original == Clone1: " + (circlePrototype == circle1));
        System.out.println("Clone1 == Clone2: " + (circle1 == circle2));
        System.out.println();
        
        // Demonstrate efficiency of cloning vs creating new
        System.out.println("5. Performance comparison (cloning vs new creation):");
        long startTime, endTime;
        
        // Time cloning (silent)
        startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            Shape clonedShape = circlePrototype.clone();
        }
        endTime = System.nanoTime();
        long cloneTime = endTime - startTime;
        
        // Time new creation (silent)
        startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            Circle newShape = new Circle();
            newShape.setColor("Red");
            newShape.setX(10);
            newShape.setY(20);
            ((Circle) newShape).setRadius(15);
        }
        endTime = System.nanoTime();
        long newTime = endTime - startTime;
        
        System.out.println("Time for 1000 clones: " + cloneTime + " nanoseconds");
        System.out.println("Time for 1000 new objects: " + newTime + " nanoseconds");
        System.out.println("Cloning is " + String.format("%.2f", (double) newTime / cloneTime) + "x faster");
        
        System.out.println("\n=== Demo Complete ===");
    }
}