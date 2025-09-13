class Prototype {
  cloneShallow() {
    throw new Error('cloneShallow() must be implemented by subclasses');
  }
  cloneDeep() {
    throw new Error('cloneDeep() must be implemented by subclasses');
  }
}

module.exports = { Prototype };
