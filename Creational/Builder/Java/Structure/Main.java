public class Main {
    public static void main(String[] args) {
        Director director = new Director();

        HouseBuilder simpleBuilder = new ConcreteHouseBuilder();
        director.constructSimpleHouse(simpleBuilder);
        House simpleHouse = simpleBuilder.getResult();

        HouseBuilder luxuryBuilder = new ConcreteHouseBuilder();
        director.constructLuxuryHouse(luxuryBuilder);
        House luxuryHouse = luxuryBuilder.getResult();

        System.out.println("Simple House: " + simpleHouse);
        System.out.println("Luxury House: " + luxuryHouse);
    }
}