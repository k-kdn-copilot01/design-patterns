package Creational.Decorator.Java.Structure;

public class Client {
    public String run() {
        Component base = new ConcreteComponent();
        String a = base.operation();
        String b = new ConcreteDecoratorA(base).operation();
        String c = new ConcreteDecoratorB(new ConcreteDecoratorA(base)).operation();
        return String.join(System.lineSeparator(), a, b, c);
    }
}
