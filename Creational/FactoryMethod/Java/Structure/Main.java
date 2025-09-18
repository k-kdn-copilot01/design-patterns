/**
 * Main class để demo Factory Method pattern với structure chuẩn
 */
public class Main {
    
    /**
     * Client code làm việc với Creator thông qua abstract interface
     */
    public static void clientCode(Creator creator) {
        System.out.println("Client: Làm việc với creator (không biết concrete class)");
        creator.someOperation();
    }
    
    public static void main(String[] args) {
        System.out.println("=== Demo Cấu Trúc: Factory Method Pattern ===\n");
        
        System.out.println("1. Sử dụng ConcreteCreatorA:");
        Creator creatorA = new ConcreteCreatorA();
        clientCode(creatorA);
        System.out.println();
        
        System.out.println("2. Sử dụng ConcreteCreatorB:");
        Creator creatorB = new ConcreteCreatorB();
        clientCode(creatorB);
        System.out.println();
        
        System.out.println("3. Minh họa tính đa hình:");
        Creator[] creators = {new ConcreteCreatorA(), new ConcreteCreatorB()};
        
        for (int i = 0; i < creators.length; i++) {
            System.out.println("Creator " + (i + 1) + ":");
            creators[i].someOperation();
            System.out.println();
        }
        
        System.out.println("=== Hoàn Thành Demo Cấu Trúc ===");
    }
}
