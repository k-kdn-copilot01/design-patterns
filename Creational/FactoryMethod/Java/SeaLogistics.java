/**
 * SeaLogistics Class (ConcreteCreator)
 * 
 * Concrete implementation của Logistics class cho vận chuyển đường biển.
 * Override factory method để tạo ra Ship object.
 */
public class SeaLogistics extends Logistics {
    
    /**
     * Factory method implementation cho sea logistics
     * Tạo và trả về Ship object
     */
    @Override
    public Transport createTransport() {
        System.out.println("🏭 SeaLogistics factory creating ship...");
        return new Ship();
    }
    
    /**
     * Trả về loại logistics
     */
    @Override
    public String getLogisticsType() {
        return "Sea Logistics";
    }
}