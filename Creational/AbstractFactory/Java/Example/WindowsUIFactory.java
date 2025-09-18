package Example;

public class WindowsUIFactory implements UIFactory {

    public Button createButton() {
        return new WindowsButton();
    }

    public TextField createTextField() {
        return new WindowsTextField();
    }
}
