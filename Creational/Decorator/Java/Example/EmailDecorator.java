package Creational.Decorator.Java.Example;

public class EmailDecorator extends NotifierDecorator {
    public EmailDecorator(Notifier wrappee) {
        super(wrappee);
    }

    @Override
    public String send() {
        return wrappee.send() + " via Email";
    }
}

