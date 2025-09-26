// Abstraction contains a reference to an Implementor
public class Abstraction {
    protected Implementor implementor;

    public Abstraction(Implementor implementor) {
        this.implementor = implementor;
    }

    public void operation(String message) {
        System.out.println("Abstraction: delegating operation for -> " + message);
        implementor.operationImpl(message);
    }

    public void changeImplementor(Implementor impl) {
        this.implementor = impl;
    }
}
