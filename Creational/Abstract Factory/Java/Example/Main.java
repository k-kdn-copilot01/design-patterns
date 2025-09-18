public class Main {
    public static void main(String[] args) {
        System.out.println("--- Abstract Factory: Furniture Example ---");

        System.out.println("Modern family:");
        FurnitureFactory modern = new ModernFurnitureFactory();
        Showroom showroom1 = new Showroom(modern);
        showroom1.demo();

        System.out.println("\nVictorian family:");
        FurnitureFactory victorian = new VictorianFurnitureFactory();
        Showroom showroom2 = new Showroom(victorian);
        showroom2.demo();

        System.out.println("\nSwap factories to get different families quickly");
        Showroom swap = new Showroom(modern);
        swap.demo();
    }
}
