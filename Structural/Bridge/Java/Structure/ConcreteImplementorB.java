public class ConcreteImplementorB implements Implementor {
    @Override
    public void operationImpl(String payload) {
        System.out.println("ConcreteImplementorB: processing -> " + payload);
    }
}
