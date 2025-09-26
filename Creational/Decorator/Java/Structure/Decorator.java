package Creational.Decorator.Java.Structure;

public abstract class Decorator implements Component {
    protected final Component wrappee;
    public Decorator(Component wrappee) {
        this.wrappee = wrappee;
    }
}
