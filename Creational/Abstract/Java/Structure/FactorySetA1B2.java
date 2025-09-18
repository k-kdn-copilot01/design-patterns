public class FactorySetA1B2 extends Factory{
    @Override
    public ProductA createProductA() {
        return new ConcreteA1();
    }

    @Override
    public ProductB createProductB() {
        return new ConcreteB1();
    }
}
