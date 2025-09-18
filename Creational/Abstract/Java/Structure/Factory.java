abstract class Factory {
    private ProductA productA;
    private ProductB productB;

    public void handleBatchProduct(){
        productA = createProductA();
        productB = createProductB();

//        Some operation with product A
//        Some operation with product B
//        Work, because both concrete of each product share the same operations
    }

    abstract ProductA createProductA();
    abstract ProductB createProductB();
}
