import { Prototype } from "./Prototype";

/**
 * Client - Uses Prototype objects to create clones
 * Demonstrates the Prototype pattern usage
 */
export class Client {
  /**
   * Client code that works with Prototype objects
   * @param prototype - Prototype instance to clone
   * @returns Result of the cloning operation
   */
  static clientCode(prototype: Prototype): string {
    const cloned = prototype.clone();
    return `Client: Cloned ${prototype.constructor.name} -> ${cloned.constructor.name}`;
  }

  /**
   * Demonstrates reference vs value comparison
   * @param original - Original object
   * @param cloned - Cloned object
   * @returns Comparison result
   */
  static compareReferences(original: any, cloned: any): string {
    const sameReference = original === cloned;
    const sameType = original.constructor.name === cloned.constructor.name;
    const sameContent = JSON.stringify(original) === JSON.stringify(cloned);

    return `Reference comparison:
- Same reference: ${sameReference}
- Same type: ${sameType}
- Same content: ${sameContent}`;
  }

  /**
   * Demonstrates shallow vs deep cloning
   * @param original - Original object with nested properties
   * @param shallowClone - Shallow cloned object
   * @param deepClone - Deep cloned object
   * @returns Comparison result
   */
  static compareCloningTypes(
    original: any,
    shallowClone: any,
    deepClone: any
  ): string {
    const originalNested =
      original.nestedObject || original.items || original.metadata;
    const shallowNested =
      shallowClone.nestedObject || shallowClone.items || shallowClone.metadata;
    const deepNested =
      deepClone.nestedObject || deepClone.items || deepClone.metadata;

    const shallowSameRef = originalNested === shallowNested;
    const deepSameRef = originalNested === deepNested;

    return `Cloning comparison:
- Shallow clone nested reference same: ${shallowSameRef}
- Deep clone nested reference same: ${deepSameRef}`;
  }
}
