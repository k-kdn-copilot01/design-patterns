package Structure;

public class FactoryProductType1 implements FactoryProduct {

    public ProductA createProductA() {
        return new ProductA1();
    }

    public ProductB createProductB() {
        return new ProductB1();
    }
}
