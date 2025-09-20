package Structural.Adapter.Example;
import java.util.Locale;

interface VietnameseTarget {
    void send(String message);
}

class JapaneseAdaptee {
    public void receive(String message) {
        System.out.println("Japanese Adaptee received: " + message);
    }
}

class JapaneseAdapter implements VietnameseTarget {
    private JapaneseAdaptee adaptee;

    public JapaneseAdapter(JapaneseAdaptee adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public void send(String message) {
        System.out.println("Vietnamese message: " + message);
        // Translator simulation
        message = message.toLowerCase(Locale.ROOT);
        adaptee.receive(message);
    }
}

public class Main {
    public static void main(String[] args) {
        VietnameseTarget client = new JapaneseAdapter(new JapaneseAdaptee());
        client.send("Xin Chao");
    }
}