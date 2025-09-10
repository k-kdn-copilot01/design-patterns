/**
 * Concrete implementation of ProductB for family 2
 */
public class ConcreteProductB2 implements ProductB {
    
    @Override
    public void operationB() {
        System.out.println("ConcreteProductB2: Operation B executed");
    }
    
    @Override
    public void collaborateWithA(ProductA productA) {
        System.out.println("ConcreteProductB2: Collaborating with " + productA.getClass().getSimpleName());
    }
}