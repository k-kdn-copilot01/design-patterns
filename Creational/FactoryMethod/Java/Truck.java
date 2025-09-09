/**
 * Truck Class (ConcreteProduct)
 * 
 * Implement cụ thể của Transport interface cho vận chuyển đường bộ.
 * Đây là một trong những sản phẩm cụ thể mà factory method có thể tạo ra.
 */
public class Truck implements Transport {
    private final double cost;
    
    public Truck() {
        this.cost = 100.0; // Chi phí vận chuyển đường bộ
        System.out.println("Truck instance created");
    }
    
    @Override
    public void deliver() {
        System.out.println("🚛 Delivering goods by TRUCK on the road");
        System.out.println("   - Loading cargo into truck container");
        System.out.println("   - Driving on highway network");
        System.out.println("   - Delivery completed at destination");
    }
    
    @Override
    public String getTransportType() {
        return "Road Transport (Truck)";
    }
    
    @Override
    public double getCost() {
        return cost;
    }
}