package Creational.Decorator.Java.Structure;

public class ConcreteDecoratorA extends Decorator {
    public ConcreteDecoratorA(Component wrappee) {
        super(wrappee);
    }

    @Override
    public String operation() {
        return wrappee.operation() + " World";
    }
}
