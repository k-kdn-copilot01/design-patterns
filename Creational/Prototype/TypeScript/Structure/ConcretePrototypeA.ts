import { Prototype } from "./Prototype";

/**
 * ConcretePrototypeA - Concrete implementation of Prototype
 * Demonstrates shallow cloning
 */
export class ConcretePrototypeA implements Prototype {
  public field1: string;
  public field2: number;
  public nestedObject: { value: string };

  constructor(
    field1: string = "",
    field2: number = 0,
    nestedValue: string = ""
  ) {
    this.field1 = field1;
    this.field2 = field2;
    this.nestedObject = { value: nestedValue };
  }

  /**
   * Creates a shallow clone of this object
   * Note: nested objects are shared between original and clone
   */
  clone(): ConcretePrototypeA {
    const cloned = new ConcretePrototypeA();
    cloned.field1 = this.field1;
    cloned.field2 = this.field2;
    cloned.nestedObject = this.nestedObject; // Shallow copy - shared reference
    return cloned;
  }

  /**
   * Creates a deep clone of this object
   * Note: nested objects are also cloned
   */
  deepClone(): ConcretePrototypeA {
    const cloned = new ConcretePrototypeA();
    cloned.field1 = this.field1;
    cloned.field2 = this.field2;
    cloned.nestedObject = { value: this.nestedObject.value }; // Deep copy - new object
    return cloned;
  }

  toString(): string {
    return `ConcretePrototypeA(field1="${this.field1}", field2=${
      this.field2
    }, nestedObject=${JSON.stringify(this.nestedObject)})`;
  }
}
