/**
 * Windows-style checkbox implementation
 */
public class WinCheckbox implements Checkbox {
    private boolean checked = false;
    
    @Override
    public void render() {
        System.out.println("Rendering Windows-style checkbox [" + (checked ? "✓" : " ") + "] Remember me");
    }
    
    @Override
    public void toggle() {
        checked = !checked;
        System.out.println("Windows checkbox toggled to: " + (checked ? "checked" : "unchecked"));
    }
    
    @Override
    public boolean isChecked() {
        return checked;
    }
}