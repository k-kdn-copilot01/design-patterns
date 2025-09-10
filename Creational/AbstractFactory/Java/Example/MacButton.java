/**
 * Mac-style button implementation
 */
public class MacButton implements Button {
    
    @Override
    public void render() {
        System.out.println("Rendering Mac-style button (Submit)");
    }
    
    @Override
    public void onClick() {
        System.out.println("Mac button clicked with Cocoa event handling");
    }
}