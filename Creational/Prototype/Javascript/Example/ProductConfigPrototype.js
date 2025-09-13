const { deepClone } = require('../Structure/utils');

class ProductConfigPrototype {
  constructor(baseConfig) {
    this.baseConfig = baseConfig;
  }

  createVariant(patch = {}) {
    const variant = deepClone(this.baseConfig);
    Object.assign(variant, patch);
    return variant;
  }
}

module.exports = { ProductConfigPrototype };
