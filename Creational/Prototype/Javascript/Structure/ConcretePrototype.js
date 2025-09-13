const { Prototype } = require('./Prototype');
const { deepClone } = require('./utils');

class DocumentPrototype extends Prototype {
  constructor({ id, title, meta, tags }) {
    super();
    this.id = id;
    this.title = title;
    this.meta = meta;
    this.tags = tags;
  }

  cloneShallow() {
    return Object.assign(Object.create(Object.getPrototypeOf(this)), this);
  }

  cloneDeep() {
    const data = deepClone({
      id: this.id,
      title: this.title,
      meta: this.meta,
      tags: this.tags
    });
    return new DocumentPrototype(data);
  }
}

module.exports = { DocumentPrototype };
