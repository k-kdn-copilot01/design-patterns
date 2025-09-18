public class Showroom {
    private Chair chair;
    private Sofa sofa;

    public Showroom(FurnitureFactory factory) {
        chair = factory.createChair();
        sofa = factory.createSofa();
    }

    public void demo() {
        System.out.println(chair.sitOn());
        System.out.println(sofa.lieOn());
    }
}
