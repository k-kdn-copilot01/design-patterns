import { Checkbox } from "./Checkbox";

/**
 * FlatCheckbox - Concrete implementation of Checkbox
 * Represents Flat Design checkbox component
 */
export class FlatCheckbox extends Checkbox {
  constructor(label: string) {
    super(label, "Flat Design");
  }

  render(): string {
    const checkedClass = this.checked ? "checked" : "";
    return `<label class="flat-checkbox ${checkedClass}" style="${this.getStyle()}">
      <input type="checkbox" ${this.checked ? "checked" : ""} />
      <span class="checkmark"></span>
      ${this.label}
    </label>`;
  }

  toggle(): string {
    this.checked = !this.checked;
    return `Flat checkbox "${this.label}" ${
      this.checked ? "checked" : "unchecked"
    }`;
  }

  getStyle(): string {
    return "display: flex; align-items: center; font-family: 'Arial', sans-serif; color: #666; cursor: pointer; font-size: 14px;";
  }
}
