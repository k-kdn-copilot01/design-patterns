package Creational.Decorator.Java.Example;

public class SmsDecorator extends NotifierDecorator {
    public SmsDecorator(Notifier wrappee) {
        super(wrappee);
    }

    @Override
    public String send() {
        return wrappee.send() + " via SMS";
    }
}

