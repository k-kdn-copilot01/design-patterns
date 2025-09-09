/**
 * Logistics Abstract Class (Creator)
 * 
 * Đây là abstract class định nghĩa factory method.
 * Các subclass sẽ override factory method để tạo ra các loại transport khác nhau.
 * 
 * Creator class cũng có thể chứa business logic khác không liên quan đến việc tạo product.
 */
public abstract class Logistics {
    
    /**
     * Factory Method - phương thức abstract mà các subclass phải implement
     * Đây là phương thức chính của Factory Method pattern
     */
    public abstract Transport createTransport();
    
    /**
     * Business logic sử dụng factory method
     * Phương thức này không biết loại transport cụ thể nào sẽ được tạo
     */
    public void planDelivery() {
        System.out.println("Planning delivery using " + getLogisticsType() + "...");
        
        // Sử dụng factory method để tạo transport
        Transport transport = createTransport();
        
        // Sử dụng transport được tạo
        System.out.println("Transport type: " + transport.getTransportType());
        System.out.println("Estimated cost: $" + transport.getCost());
        
        // Thực hiện vận chuyển
        transport.deliver();
        
        System.out.println("Delivery planning completed!\n");
    }
    
    /**
     * Phương thức trả về loại logistics - được override bởi concrete classes
     */
    public abstract String getLogisticsType();
}