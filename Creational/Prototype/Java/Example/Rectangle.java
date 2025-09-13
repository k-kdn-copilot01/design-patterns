/**
 * Rectangle implementation of Shape prototype
 */
public class Rectangle extends Shape {
    private double width;
    private double height;
    
    public Rectangle() {}
    
    public Rectangle(double width, double height, String color, int x, int y) {
        this.width = width;
        this.height = height;
        this.color = color;
        this.x = x;
        this.y = y;
        System.out.println("Rectangle created: " + width + "x" + height + ", color=" + color);
    }
    
    public Rectangle(Rectangle other) {
        super(other);
        if (other != null) {
            this.width = other.width;
            this.height = other.height;
        }
        System.out.println("Rectangle cloned: " + width + "x" + height + ", color=" + color);
    }
    
    @Override
    public Prototype clone() {
        return new Rectangle(this);
    }
    
    @Override
    public String getInfo() {
        return String.format("Rectangle[width=%.1f, height=%.1f, color='%s', position=(%d,%d), area=%.2f]", 
                           width, height, color, x, y, getArea());
    }
    
    @Override
    public double getArea() {
        return width * height;
    }
    
    public double getWidth() {
        return width;
    }
    
    public double getHeight() {
        return height;
    }
    
    public void setWidth(double width) {
        this.width = width;
    }
    
    public void setHeight(double height) {
        this.height = height;
    }
}