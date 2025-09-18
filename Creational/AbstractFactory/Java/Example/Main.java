package Example;

public class Main {

    public static void main(String[] args) {
        System.out.println("=== Windows UI ===");
        UIFactory windowsFactory = new WindowsUIFactory();
        Button windowsButton = windowsFactory.createButton();
        TextField windowsTextField = windowsFactory.createTextField();
        windowsButton.render();
        windowsTextField.render();

        System.out.println("\n=== Mac UI ===");
        UIFactory macFactory = new MacUIFactory();
        Button macButton = macFactory.createButton();
        TextField macTextField = macFactory.createTextField();
        macButton.render();
        macTextField.render();
    }
}
