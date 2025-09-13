const { DocumentPrototype } = require('./ConcretePrototype');

function runStructureDemo() {
  const original = new DocumentPrototype({
    id: 1,
    title: 'Design Patterns Spec',
    meta: { author: { name: 'Alice' }, pages: 120 },
    tags: ['patterns', 'oop']
  });

  const shallow = original.cloneShallow();
  const deep = original.cloneDeep();

  console.log('original === shallow', original === shallow);
  console.log('original === deep', original === deep);

  console.log('original.meta === shallow.meta', original.meta === shallow.meta);
  console.log('original.meta === deep.meta', original.meta === deep.meta); 

  shallow.meta.author.name = 'Nam';
  shallow.tags.push('shallow-edit');

  deep.meta.pages = 200;
  deep.tags.push('deep-edit');

  console.log('name =>', original.meta.author.name);
  console.log('page', deep.meta.pages);
  console.log('pages', original.meta.pages);

  console.log('original.tags', original.tags);
  console.log('deep.tags', deep.tags);     

  console.log('original.tags === shallow.tags', original.tags === shallow.tags);
  console.log('original.tags === deep.tags', original.tags === deep.tags);
}

module.exports = { runStructureDemo };
