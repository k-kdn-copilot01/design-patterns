/**
 * Product interface - định nghĩa interface chung cho tất cả products
 * được tạo ra bởi factory method
 */
public interface Product {
    /**
     * Phương thức chung mà tất cả concrete products phải implement
     */
    void operation();
    
    /**
     * Trả về tên của product
     */
    String getName();
}
