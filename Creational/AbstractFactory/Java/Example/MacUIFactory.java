package Example;

public class MacUIFactory implements UIFactory {

    public Button createButton() {
        return new MacButton();
    }

    public TextField createTextField() {
        return new MacTextField();
    }
}
