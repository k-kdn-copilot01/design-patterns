abstract class Shop {
    private Fruit fruit;

    public void sell(){
        fruit = createFruit();

        fruit.prepareFruit();
        fruit.transferFruit();
        fruit.getMoney();
    }

    abstract Fruit createFruit();
}
