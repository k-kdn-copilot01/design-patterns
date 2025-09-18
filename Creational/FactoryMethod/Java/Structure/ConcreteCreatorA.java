/**
 * ConcreteCreatorA - implementation cụ thể của Creator
 * Override factory method để tạo ConcreteProductA
 */
public class ConcreteCreatorA extends Creator {
    
    @Override
    public Product factoryMethod() {
        System.out.println("ConcreteCreatorA: Tạo Product A");
        return new ConcreteProductA();
    }
}
