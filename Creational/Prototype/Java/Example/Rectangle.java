/**
 * Rectangle - Concrete Prototype
 * 
 * Another concrete shape that demonstrates the prototype pattern
 * with different properties than Circle.
 */
public class Rectangle extends Shape {
    private int width;
    private int height;
    
    public Rectangle() {
    }
    
    public Rectangle(Rectangle target) {
        super(target);
        if (target != null) {
            this.width = target.width;
            this.height = target.height;
        }
    }
    
    public Rectangle(String color, int x, int y, int width, int height) {
        this.color = color;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        System.out.println("Rectangle created: " + this.toString());
    }
    
    @Override
    public Shape clone() {
        return new Rectangle(this);
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing Rectangle at (" + x + "," + y + ") with size " + width + "x" + height + " in " + color);
    }
    
    @Override
    public double getArea() {
        return width * height;
    }
    
    public int getWidth() {
        return width;
    }
    
    public void setWidth(int width) {
        this.width = width;
    }
    
    public int getHeight() {
        return height;
    }
    
    public void setHeight(int height) {
        this.height = height;
    }
    
    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Rectangle) || !super.equals(object)) return false;
        Rectangle rectangle = (Rectangle) object;
        return rectangle.width == width && rectangle.height == height;
    }
    
    @Override
    public String toString() {
        return "Rectangle[color=" + color + ", x=" + x + ", y=" + y + ", width=" + width + ", height=" + height + "]";
    }
}