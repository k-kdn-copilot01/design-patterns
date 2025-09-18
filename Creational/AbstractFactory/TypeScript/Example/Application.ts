import { UIFactory } from "./UIFactory";
import { Button } from "./Button";
import { Checkbox } from "./Checkbox";

/**
 * Application - Client that uses UIFactory to create and work with UI components
 * Demonstrates the Abstract Factory pattern usage in real-world UI scenario
 */
export class Application {
  private factory: UIFactory;
  private components: Array<{ type: string; component: Button | Checkbox }> =
    [];

  constructor(factory: UIFactory) {
    this.factory = factory;
  }

  /**
   * Sets a new UI factory
   */
  setFactory(factory: UIFactory): void {
    this.factory = factory;
  }

  /**
   * Gets the current UI factory
   */
  getFactory(): UIFactory {
    return this.factory;
  }

  /**
   * Creates a UI component and adds it to the application
   */
  createComponent(
    type: "button" | "checkbox",
    text: string
  ): Button | Checkbox {
    let component: Button | Checkbox;

    if (type === "button") {
      component = this.factory.createButton(text);
    } else {
      component = this.factory.createCheckbox(text);
    }

    this.components.push({ type, component });
    return component;
  }

  /**
   * Renders all components
   */
  renderAll(): string {
    let result = `=== ${this.factory.getDesignSystem()} Application ===\n\n`;

    this.components.forEach((item, index) => {
      result += `Component ${index + 1} (${item.type}):\n`;
      result += item.component.render();
      result += "\n\n";
    });

    return result;
  }

  /**
   * Demonstrates component interaction
   */
  demonstrateInteraction(): string {
    let result = `=== Component Interaction Demo ===\n\n`;

    this.components.forEach((item, index) => {
      result += `Component ${index + 1}:\n`;

      if (item.type === "button") {
        result += `- Click: ${(item.component as Button).onClick()}\n`;
      } else {
        result += `- Toggle: ${(item.component as Checkbox).toggle()}\n`;
      }

      result += `- Style: ${item.component.getStyle()}\n`;
      result += `- Theme: ${item.component.getTheme()}\n\n`;
    });

    return result;
  }

  /**
   * Gets all components
   */
  getAllComponents(): Array<{ type: string; component: Button | Checkbox }> {
    return [...this.components];
  }

  /**
   * Clears all components
   */
  clear(): void {
    this.components = [];
  }

  /**
   * Gets component statistics
   */
  getStatistics(): string {
    const buttonCount = this.components.filter(
      (c) => c.type === "button"
    ).length;
    const checkboxCount = this.components.filter(
      (c) => c.type === "checkbox"
    ).length;

    return `Application Statistics:
Design System: ${this.factory.getDesignSystem()}
Theme: ${this.factory.getTheme()}
Total Components: ${this.components.length}
- Buttons: ${buttonCount}
- Checkboxes: ${checkboxCount}`;
  }
}
