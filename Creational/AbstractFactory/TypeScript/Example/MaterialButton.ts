import { Button } from "./Button";

/**
 * MaterialButton - Concrete implementation of Button
 * Represents Material Design button component
 */
export class MaterialButton extends Button {
  constructor(text: string) {
    super(text, "Material Design");
  }

  render(): string {
    return `<button class="material-button" style="${this.getStyle()}">${
      this.text
    }</button>`;
  }

  onClick(): string {
    return `Material button "${this.text}" clicked with ripple effect`;
  }

  getStyle(): string {
    return "background: #2196F3; color: white; border: none; padding: 12px 24px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.2); font-family: 'Roboto', sans-serif;";
  }
}
