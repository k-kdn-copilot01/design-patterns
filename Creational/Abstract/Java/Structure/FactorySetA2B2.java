public class FactorySetA2B2 extends Factory {
    @Override
    public ProductB createProductB() {
        return new ConcreteB2();
    }

    @Override
    public ProductA createProductA() {
        return new ConcreteA2();
    }
}
