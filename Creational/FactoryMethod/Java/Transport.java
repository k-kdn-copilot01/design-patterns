/**
 * Transport Interface (Product)
 * 
 * Định nghĩa interface chung cho tất cả các sản phẩm mà factory method có thể tạo ra.
 * Trong ví dụ này, Transport đại diện cho phương tiện vận chuyển.
 */
public interface Transport {
    /**
     * Phương thức vận chuyển - được implement khác nhau bởi mỗi loại transport
     */
    void deliver();
    
    /**
     * Lấy thông tin về loại phương tiện vận chuyển
     */
    String getTransportType();
    
    /**
     * Lấy thông tin về chi phí vận chuyển
     */
    double getCost();
}