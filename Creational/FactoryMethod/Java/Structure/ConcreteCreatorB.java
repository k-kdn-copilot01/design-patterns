/**
 * ConcreteCreatorB - implementation cụ thể khác của Creator
 * Override factory method để tạo ConcreteProductB
 */
public class ConcreteCreatorB extends Creator {
    
    @Override
    public Product factoryMethod() {
        System.out.println("ConcreteCreatorB: Tạo Product B");
        return new ConcreteProductB();
    }
}
