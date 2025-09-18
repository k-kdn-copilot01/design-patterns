public class WatermelonShop extends Shop {
    @Override
    public Fruit createFruit() {
        return new Watermelon(20);
    }
}
