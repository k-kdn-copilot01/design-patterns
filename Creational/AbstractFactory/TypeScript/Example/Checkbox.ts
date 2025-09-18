/**
 * Checkbox - Abstract base class for all checkbox components
 * Defines the interface for all checkbox variants
 */
export abstract class Checkbox {
  protected label: string;
  protected theme: string;
  protected checked: boolean = false;

  constructor(label: string, theme: string) {
    this.label = label;
    this.theme = theme;
  }

  /**
   * Renders the checkbox
   */
  abstract render(): string;

  /**
   * Handles toggle events
   */
  abstract toggle(): string;

  /**
   * Gets the checkbox style
   */
  abstract getStyle(): string;

  /**
   * Gets the theme name
   */
  getTheme(): string {
    return this.theme;
  }

  /**
   * Gets the checkbox label
   */
  getLabel(): string {
    return this.label;
  }

  /**
   * Checks if the checkbox is checked
   */
  isChecked(): boolean {
    return this.checked;
  }

  /**
   * Sets the checked state
   */
  setChecked(checked: boolean): void {
    this.checked = checked;
  }
}
