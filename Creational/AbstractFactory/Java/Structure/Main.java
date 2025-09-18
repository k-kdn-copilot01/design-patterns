package Structure;

public class Main {

    public static void main(String[] args) {
        // Demo with Factory Type 1
        System.out.println("=== Demo Factory Type 1 ===");
        FactoryProduct factory1 = new FactoryProductType1();

        ProductA productA1 = factory1.createProductA();
        ProductB productB1 = factory1.createProductB();

        productA1.actionProductA();
        productB1.actionProductB();

        // Demo with Factory Type 2
        System.out.println("\n=== Demo Factory Type 2 ===");
        FactoryProduct factory2 = new FactoryProductType2();

        ProductA productA2 = factory2.createProductA();
        ProductB productB2 = factory2.createProductB();

        productA2.actionProductA();
        productB2.actionProductB();
    }
}
