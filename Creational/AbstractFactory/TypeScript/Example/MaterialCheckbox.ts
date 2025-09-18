import { Checkbox } from "./Checkbox";

/**
 * MaterialCheckbox - Concrete implementation of Checkbox
 * Represents Material Design checkbox component
 */
export class MaterialCheckbox extends Checkbox {
  constructor(label: string) {
    super(label, "Material Design");
  }

  render(): string {
    const checkedClass = this.checked ? "checked" : "";
    return `<label class="material-checkbox ${checkedClass}" style="${this.getStyle()}">
      <input type="checkbox" ${this.checked ? "checked" : ""} />
      <span class="checkmark"></span>
      ${this.label}
    </label>`;
  }

  toggle(): string {
    this.checked = !this.checked;
    return `Material checkbox "${this.label}" ${
      this.checked ? "checked" : "unchecked"
    }`;
  }

  getStyle(): string {
    return "display: flex; align-items: center; font-family: 'Roboto', sans-serif; color: #333; cursor: pointer;";
  }
}
