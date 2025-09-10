/**
 * Circle - Concrete Prototype
 * 
 * A concrete shape that can be cloned. Demonstrates prototype pattern
 * with a real geometric shape including specific properties.
 */
public class Circle extends Shape {
    private int radius;
    
    public Circle() {
    }
    
    public Circle(Circle target) {
        super(target);
        if (target != null) {
            this.radius = target.radius;
        }
    }
    
    public Circle(String color, int x, int y, int radius) {
        this.color = color;
        this.x = x;
        this.y = y;
        this.radius = radius;
        System.out.println("Circle created: " + this.toString());
    }
    
    @Override
    public Shape clone() {
        return new Circle(this);
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing Circle at (" + x + "," + y + ") with radius " + radius + " in " + color);
    }
    
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
    
    public int getRadius() {
        return radius;
    }
    
    public void setRadius(int radius) {
        this.radius = radius;
    }
    
    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Circle) || !super.equals(object)) return false;
        Circle circle = (Circle) object;
        return circle.radius == radius;
    }
    
    @Override
    public String toString() {
        return "Circle[color=" + color + ", x=" + x + ", y=" + y + ", radius=" + radius + "]";
    }
}