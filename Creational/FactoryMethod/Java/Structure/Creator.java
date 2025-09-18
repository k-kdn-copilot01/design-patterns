/**
 * Creator abstract class - định nghĩa factory method
 * và có thể chứa business logic khác
 */
public abstract class Creator {
    
    /**
     * Factory Method - phương thức abstract để tạo Product
     * Các subclass sẽ override để tạo concrete product cụ thể
     */
    public abstract Product factoryMethod();
    
    /**
     * Business logic sử dụng factory method
     * Lưu ý: method này gọi factoryMethod() nhưng không biết
     * concrete product nào sẽ được tạo ra
     */
    public void someOperation() {
        System.out.println("Creator: Bắt đầu thực hiện nghiệp vụ...");
        
        // Gọi factory method để tạo product
        Product product = factoryMethod();
        
        System.out.println("Creator: Đang làm việc với " + product.getName());
        product.operation();
        
        System.out.println("Creator: Hoàn thành thực hiện nghiệp vụ.");
    }
}
