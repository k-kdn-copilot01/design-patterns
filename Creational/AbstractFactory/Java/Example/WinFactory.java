/**
 * Windows-style UI factory
 */
public class WinFactory implements UIFactory {
    
    @Override
    public Button createButton() {
        return new WinButton();
    }
    
    @Override 
    public Checkbox createCheckbox() {
        return new WinCheckbox();
    }
}