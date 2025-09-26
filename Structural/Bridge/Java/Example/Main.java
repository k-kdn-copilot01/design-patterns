public class Main {
    public static void main(String[] args) {
        System.out.println("--- Bridge Pattern: Shape Drawing Example ---");

        DrawingAPI api1 = new DrawingAPI1();
        DrawingAPI api2 = new DrawingAPI2();

        Shape circle1 = new CircleShape(1, 2, 3, api1);
        Shape circle2 = new CircleShape(5, 7, 11, api2);

        System.out.println("Draw with API1:");
        circle1.draw();

        System.out.println("Draw with API2:");
        circle2.draw();

        System.out.println("Resize circle1 by 50% and redraw using API1:");
        circle1.resizeByPercentage(50);
        circle1.draw();

        System.out.println("Swap implementor of circle1 to API2 and draw:");
        circle1.drawingAPI = api2; // show runtime swap
        circle1.draw();
    }
}
