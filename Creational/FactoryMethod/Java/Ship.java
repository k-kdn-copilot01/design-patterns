/**
 * Ship Class (ConcreteProduct)
 * 
 * Implement cụ thể của Transport interface cho vận chuyển đường biển.
 * Đây là một trong những sản phẩm cụ thể mà factory method có thể tạo ra.
 */
public class Ship implements Transport {
    private final double cost;
    
    public Ship() {
        this.cost = 250.0; // Chi phí vận chuyển đường biển
        System.out.println("Ship instance created");
    }
    
    @Override
    public void deliver() {
        System.out.println("🚢 Delivering goods by SHIP across the ocean");
        System.out.println("   - Loading cargo into ship containers");
        System.out.println("   - Navigating through sea routes");
        System.out.println("   - Delivery completed at port destination");
    }
    
    @Override
    public String getTransportType() {
        return "Sea Transport (Ship)";
    }
    
    @Override
    public double getCost() {
        return cost;
    }
}