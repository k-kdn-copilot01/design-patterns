abstract class Creator {
    private Product product;

    public void process(){
        // We use the product to do something here. Because the procedure of each product is the same, so we can code it here and apply it to overall
        product =  createProduct();

        product.step1();
        product.step2();
        product.step3();
    }

    abstract Product createProduct();

}
