package Creational.Decorator.Java.Structure;

public class ConcreteDecoratorB extends Decorator {
    public ConcreteDecoratorB(Component wrappee) {
        super(wrappee);
    }

    @Override
    public String operation() {
        return wrappee.operation() + "!";
    }
}
