import { UIFactory } from "./UIFactory";
import { FlatButton } from "./FlatButton";
import { FlatCheckbox } from "./FlatCheckbox";

/**
 * FlatUIFactory - Concrete implementation of UIFactory
 * Creates Flat Design UI components
 */
export class FlatUIFactory extends UIFactory {
  createButton(text: string): FlatButton {
    return new FlatButton(text);
  }

  createCheckbox(label: string): FlatCheckbox {
    return new FlatCheckbox(label);
  }

  getDesignSystem(): string {
    return "Flat Design";
  }

  getTheme(): string {
    return "Flat";
  }
}
