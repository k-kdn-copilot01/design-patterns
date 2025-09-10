/**
 * Mac-style checkbox implementation
 */
public class MacCheckbox implements Checkbox {
    private boolean checked = false;
    
    @Override
    public void render() {
        System.out.println("Rendering Mac-style checkbox (" + (checked ? "✓" : " ") + ") Remember me");
    }
    
    @Override
    public void toggle() {
        checked = !checked;
        System.out.println("Mac checkbox toggled to: " + (checked ? "checked" : "unchecked"));
    }
    
    @Override
    public boolean isChecked() {
        return checked;
    }
}