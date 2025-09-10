/**
 * Abstract factory for creating UI components
 */
public interface UIFactory {
    Button createButton();
    Checkbox createCheckbox();
}