/**
 * ConcreteProductA - implementation cụ thể của Product
 */
public class ConcreteProductA implements Product {
    
    @Override
    public void operation() {
        System.out.println("ConcreteProductA đang thực hiện thao tác");
    }
    
    @Override
    public String getName() {
        return "Sản phẩm A";
    }
}
