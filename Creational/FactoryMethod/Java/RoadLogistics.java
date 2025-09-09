/**
 * RoadLogistics Class (ConcreteCreator)
 * 
 * Concrete implementation của Logistics class cho vận chuyển đường bộ.
 * Override factory method để tạo ra Truck object.
 */
public class RoadLogistics extends Logistics {
    
    /**
     * Factory method implementation cho road logistics
     * Tạo và trả về Truck object
     */
    @Override
    public Transport createTransport() {
        System.out.println("🏭 RoadLogistics factory creating truck...");
        return new Truck();
    }
    
    /**
     * Trả về loại logistics
     */
    @Override
    public String getLogisticsType() {
        return "Road Logistics";
    }
}