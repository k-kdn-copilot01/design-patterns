public class ConcreteImplementorA implements Implementor {
    @Override
    public void operationImpl(String payload) {
        System.out.println("ConcreteImplementorA: handling -> " + payload);
    }
}
