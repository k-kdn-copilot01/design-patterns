/**
 * Prototype - Interface for cloneable objects
 * Defines the contract for objects that can be cloned
 */
export interface Prototype {
  /**
   * Creates a clone of the current object
   * @returns A new instance that is a copy of the current object
   */
  clone(): Prototype;
}
