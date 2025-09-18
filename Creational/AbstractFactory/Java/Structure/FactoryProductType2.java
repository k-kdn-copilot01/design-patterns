package Structure;

public class FactoryProductType2 implements FactoryProduct {

    public ProductA createProductA() {
        return new ProductA2();
    }

    public ProductB createProductB() {
        return new ProductB2();
    }
}
