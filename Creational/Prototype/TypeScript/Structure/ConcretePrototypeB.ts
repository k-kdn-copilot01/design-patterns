import { Prototype } from "./Prototype";

/**
 * ConcretePrototypeB - Another concrete implementation of Prototype
 * Demonstrates different cloning behavior
 */
export class ConcretePrototypeB implements Prototype {
  public name: string;
  public items: string[];
  public metadata: { created: Date; version: number };

  constructor(name: string = "", items: string[] = [], version: number = 1) {
    this.name = name;
    this.items = [...items]; // Copy array
    this.metadata = { created: new Date(), version };
  }

  /**
   * Creates a shallow clone of this object
   * Note: arrays and nested objects are shared between original and clone
   */
  clone(): ConcretePrototypeB {
    const cloned = new ConcretePrototypeB();
    cloned.name = this.name;
    cloned.items = this.items; // Shallow copy - shared reference
    cloned.metadata = this.metadata; // Shallow copy - shared reference
    return cloned;
  }

  /**
   * Creates a deep clone of this object
   * Note: arrays and nested objects are also cloned
   */
  deepClone(): ConcretePrototypeB {
    const cloned = new ConcretePrototypeB();
    cloned.name = this.name;
    cloned.items = [...this.items]; // Deep copy - new array
    cloned.metadata = {
      created: new Date(this.metadata.created.getTime()), // Deep copy - new Date
      version: this.metadata.version,
    };
    return cloned;
  }

  addItem(item: string): void {
    this.items.push(item);
  }

  toString(): string {
    return `ConcretePrototypeB(name="${this.name}", items=[${this.items.join(
      ", "
    )}], metadata=${JSON.stringify(this.metadata)})`;
  }
}
