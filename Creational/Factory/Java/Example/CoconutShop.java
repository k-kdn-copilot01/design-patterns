public class CoconutShop extends Shop{
    @Override
    public Fruit createFruit() {
        return new Coconut();
    }
}
