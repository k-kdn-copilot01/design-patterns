public class Main {
    public static void main(String[] args) {
        System.out.println("=== Factory Method Pattern Demo ===");

        Creator creatorA = new ConcreteCreatorA();
        Creator creatorB = new ConcreteCreatorB();

        System.out.println("\nUsing ConcreteCreatorA:");
        creatorA.someOperation();

        System.out.println("\nUsing ConcreteCreatorB:");
        creatorB.someOperation();

        System.out.println("\nDirect factory method calls:");
        Product productA = creatorA.createProduct();
        Product productB = creatorB.createProduct();

        System.out.print("Product A: ");
        productA.doStuff();
        System.out.print("Product B: ");
        productB.doStuff();
    }
}
