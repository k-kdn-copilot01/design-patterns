/**
 * Concrete implementation of ProductB for family 1
 */
public class ConcreteProductB1 implements ProductB {
    
    @Override
    public void operationB() {
        System.out.println("ConcreteProductB1: Operation B executed");
    }
    
    @Override
    public void collaborateWithA(ProductA productA) {
        System.out.println("ConcreteProductB1: Collaborating with " + productA.getClass().getSimpleName());
    }
}