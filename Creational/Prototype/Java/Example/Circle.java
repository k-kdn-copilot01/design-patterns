/**
 * Circle implementation of Shape prototype
 */
public class Circle extends Shape {
    private double radius;
    
    public Circle() {}
    
    public Circle(double radius, String color, int x, int y) {
        this.radius = radius;
        this.color = color;
        this.x = x;
        this.y = y;
        System.out.println("Circle created: radius=" + radius + ", color=" + color);
    }
    
    public Circle(Circle other) {
        super(other);
        if (other != null) {
            this.radius = other.radius;
        }
        System.out.println("Circle cloned: radius=" + radius + ", color=" + color);
    }
    
    @Override
    public Prototype clone() {
        return new Circle(this);
    }
    
    @Override
    public String getInfo() {
        return String.format("Circle[radius=%.1f, color='%s', position=(%d,%d), area=%.2f]", 
                           radius, color, x, y, getArea());
    }
    
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
    
    public double getRadius() {
        return radius;
    }
    
    public void setRadius(double radius) {
        this.radius = radius;
    }
}