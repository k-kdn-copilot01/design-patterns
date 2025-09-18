public class Main {
    public static void main(String[] args) {
        String lock = "concrete_product_2";
        Creator creator;
        if(lock.equals("concrete_product_1")){
            creator = new ConcreteCreator1();
        } else {
            creator = new ConcreteCreator2();
        }

        creator.process();
    }
}