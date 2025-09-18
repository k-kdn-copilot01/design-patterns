public abstract class Creator {
    public abstract Product createProduct();
    
    public void someOperation() {
        Product product = createProduct();
        product.doStuff();
    }
}
