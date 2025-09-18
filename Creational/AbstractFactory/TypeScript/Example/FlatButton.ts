import { Button } from "./Button";

/**
 * FlatButton - Concrete implementation of Button
 * Represents Flat Design button component
 */
export class FlatButton extends Button {
  constructor(text: string) {
    super(text, "Flat Design");
  }

  render(): string {
    return `<button class="flat-button" style="${this.getStyle()}">${
      this.text
    }</button>`;
  }

  onClick(): string {
    return `Flat button "${this.text}" clicked with smooth transition`;
  }

  getStyle(): string {
    return "background: #E91E63; color: white; border: none; padding: 10px 20px; border-radius: 0; font-family: 'Arial', sans-serif; transition: all 0.3s ease;";
  }
}
