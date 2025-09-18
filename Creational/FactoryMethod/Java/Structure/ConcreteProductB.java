/**
 * ConcreteProductB - implementation cụ thể khác của Product
 */
public class ConcreteProductB implements Product {
    
    @Override
    public void operation() {
        System.out.println("ConcreteProductB đang thực hiện thao tác");
    }
    
    @Override
    public String getName() {
        return "Sản phẩm B";
    }
}
