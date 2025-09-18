import { Button } from "./Button";
import { Checkbox } from "./Checkbox";

/**
 * UIFactory - Abstract base class for all UI factories
 * Defines the interface for creating families of UI components
 */
export abstract class UIFactory {
  /**
   * Creates a button component
   */
  abstract createButton(text: string): Button;

  /**
   * Creates a checkbox component
   */
  abstract createCheckbox(label: string): Checkbox;

  /**
   * Gets the design system name this factory creates
   */
  abstract getDesignSystem(): string;

  /**
   * Gets the theme name
   */
  abstract getTheme(): string;
}
