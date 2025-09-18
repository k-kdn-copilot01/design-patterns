package Creational.Builder.Java.Example;

public class Main {
    public static void main(String[] args) {
        Product product = new Product.Builder()
                .id("P001")
                .name("Laptop")
                .price(999.99f)
                .build();

        System.out.println("Product ID: " + product.getId());
        System.out.println("Product Name: " + product.getName());
        System.out.println("Product Price: $" + product.getPrice());

        Product product2 = new Product.Builder()
                .id("P002")
                .name("Smartphone")
                .build();

        System.out.println("Product ID: " + product2.getId());
        System.out.println("Product Name: " + product2.getName());
        System.out.println("Product Price: $" + product2.getPrice());
    }
}
