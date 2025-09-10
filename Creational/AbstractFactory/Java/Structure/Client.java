/**
 * Client class that uses AbstractFactory to create families of related products
 * without knowing the concrete classes
 */
public class Client {
    private AbstractFactory factory;
    
    public Client(AbstractFactory factory) {
        this.factory = factory;
    }
    
    public void run() {
        System.out.println("Client: Creating products using " + factory.getClass().getSimpleName());
        
        ProductA productA = factory.createProductA();
        ProductB productB = factory.createProductB();
        
        productA.operationA();
        productB.operationB();
        productB.collaborateWithA(productA);
        
        System.out.println();
    }
}