/**
 * Application client that uses UI components created by abstract factory
 */
public class Application {
    private UIFactory factory;
    private Button button;
    private Checkbox checkbox;
    
    public Application(UIFactory factory) {
        this.factory = factory;
        createUI();
    }
    
    private void createUI() {
        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
    }
    
    public void render() {
        System.out.println("Application: Rendering UI using " + factory.getClass().getSimpleName());
        button.render();
        checkbox.render();
        System.out.println();
    }
    
    public void handleUserInteraction() {
        System.out.println("Application: Simulating user interaction...");
        button.onClick();
        checkbox.toggle();
        System.out.println("Checkbox state: " + (checkbox.isChecked() ? "checked" : "unchecked"));
        System.out.println();
    }
}