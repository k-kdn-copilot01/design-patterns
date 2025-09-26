package Creational.Decorator.Java.Example;

public class Client {
    public String run() {
        Notifier base = new BasicNotifier();
        String a = base.send();
        String b = new EmailDecorator(base).send();
        String c = new SmsDecorator(new EmailDecorator(base)).send();
        return String.join(System.lineSeparator(), a, b, c);
    }
}

