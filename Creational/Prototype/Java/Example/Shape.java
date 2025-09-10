import java.util.ArrayList;
import java.util.List;

/**
 * Shape - Abstract Prototype
 * 
 * Base class for all geometric shapes that can be cloned.
 * Demonstrates a real-world use case for the Prototype pattern.
 */
public abstract class Shape {
    protected String color;
    protected int x;
    protected int y;
    
    public Shape() {
    }
    
    public Shape(Shape target) {
        if (target != null) {
            this.color = target.color;
            this.x = target.x;
            this.y = target.y;
        }
    }
    
    public abstract Shape clone();
    
    public abstract void draw();
    
    public abstract double getArea();
    
    // Getters and setters
    public String getColor() {
        return color;
    }
    
    public void setColor(String color) {
        this.color = color;
    }
    
    public int getX() {
        return x;
    }
    
    public void setX(int x) {
        this.x = x;
    }
    
    public int getY() {
        return y;
    }
    
    public void setY(int y) {
        this.y = y;
    }
    
    public void move(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Shape)) return false;
        Shape shape = (Shape) object;
        return shape.color.equals(color) && shape.x == x && shape.y == y;
    }
}