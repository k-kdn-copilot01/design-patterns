import { UIFactory } from "./UIFactory";
import { MaterialButton } from "./MaterialButton";
import { MaterialCheckbox } from "./MaterialCheckbox";

/**
 * MaterialUIFactory - Concrete implementation of UIFactory
 * Creates Material Design UI components
 */
export class MaterialUIFactory extends UIFactory {
  createButton(text: string): MaterialButton {
    return new MaterialButton(text);
  }

  createCheckbox(label: string): MaterialCheckbox {
    return new MaterialCheckbox(label);
  }

  getDesignSystem(): string {
    return "Material Design";
  }

  getTheme(): string {
    return "Material";
  }
}
