public class Watermelon implements Fruit{
    private Integer cost;

    public Watermelon(Integer cost) {
        this.cost = cost;
    }

    public Integer getCost() {
        return cost;
    }

    @Override
    public void prepareFruit() {
        System.out.println("This watermelon weight come from Europe");
    }

    @Override
    public void transferFruit() {
        System.out.println("I will cut it into slice for you");
    }

    @Override
    public void getMoney() {
        System.out.println("You will need to pay " + cost + "$ for each kg");
    }
}
