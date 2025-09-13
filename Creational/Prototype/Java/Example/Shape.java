/**
 * Shape represents a geometric shape prototype
 * Demonstrates cloning with different shape types
 */
public abstract class Shape implements Prototype {
    protected String color;
    protected int x, y;
    
    public Shape() {}
    
    public Shape(Shape other) {
        if (other != null) {
            this.color = other.color;
            this.x = other.x;
            this.y = other.y;
        }
    }
    
    public abstract Prototype clone();
    public abstract String getInfo();
    public abstract double getArea();
    
    public void setColor(String color) {
        this.color = color;
    }
    
    public void setPosition(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public String getColor() {
        return color;
    }
}