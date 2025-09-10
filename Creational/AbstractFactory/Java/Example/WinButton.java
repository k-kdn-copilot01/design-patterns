/**
 * Windows-style button implementation
 */
public class WinButton implements Button {
    
    @Override
    public void render() {
        System.out.println("Rendering Windows-style button [Submit]");
    }
    
    @Override
    public void onClick() {
        System.out.println("Windows button clicked with Windows event handling");
    }
}