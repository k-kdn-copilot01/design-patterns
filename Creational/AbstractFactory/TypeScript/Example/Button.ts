/**
 * Button - Abstract base class for all button components
 * Defines the interface for all button variants
 */
export abstract class Button {
  protected text: string;
  protected theme: string;

  constructor(text: string, theme: string) {
    this.text = text;
    this.theme = theme;
  }

  /**
   * Renders the button
   */
  abstract render(): string;

  /**
   * Handles click events
   */
  abstract onClick(): string;

  /**
   * Gets the button style
   */
  abstract getStyle(): string;

  /**
   * Gets the theme name
   */
  getTheme(): string {
    return this.theme;
  }

  /**
   * Gets the button text
   */
  getText(): string {
    return this.text;
  }
}
