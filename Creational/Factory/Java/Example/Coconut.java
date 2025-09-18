public class Coconut implements Fruit{

    @Override
    public void prepareFruit() {
        System.out.println("This coconut come from Asia");
    }

    @Override
    public void transferFruit() {
        System.out.println("I will pick it into the nilon for you");
    }

    @Override
    public void getMoney() {
        System.out.println("This's just a gift for you");
    }
}
