const { ProductConfigPrototype } = require('./ProductConfigPrototype');

function runExample() {
  const base = {
    name: 'JunSocial',
    features: {
      uploads: { maxSizeMB: 2000, chunk: true },
      analytics: { enabled: true, sampling: 0.25 },
      ai: { summarization: true, moderation: { enabled: true, vendor: 'OpenAI' } }
    },
    limits: { users: 1000, projects: 10 },
    price: 0
  };

  const configFactory = new ProductConfigPrototype(base);

  const FREE = configFactory.createVariant({
    name: 'JunSocial FREE',
    limits: { users: 100, projects: 1 },
    price: 0
  });

  const PRO = configFactory.createVariant({
    name: 'JunSocial PRO',
    limits: { users: 5000, projects: 50 },
    price: 19
  });

  const ENTERPRISE = configFactory.createVariant({
    name: 'JunSocial ENTERPRISE',
    limits: { users: 100000, projects: 1000 },
    features: {
      analytics: { enabled: true, sampling: 1.0 },
      ai: { summarization: true, moderation: { enabled: true, vendor: 'Custom' } }
    },
    price: 999
  });

  console.log('base === FREE', base === FREE);
  console.log('base === PRO', base === PRO);
  console.log('base === ENT', base === ENTERPRISE);

  FREE.features.ai.moderation.vendor = 'LiteVendor';
  console.log('FREE.features.ai.moderation.vendor', FREE.features.ai.moderation.vendor);
  console.log('base.features.ai.moderation.vendor', base.features.ai.moderation.vendor);

  PRO.limits.users = 12345;
  console.log('PRO.limits.users', PRO.limits.users);
  console.log('ENTERPRISE.limits.users', ENTERPRISE.limits.users);

  console.log({ FREE: { limits: FREE.limits, price: FREE.price } });
  console.log({ PRO: { limits: PRO.limits, price: PRO.price } });
  console.log({ ENTERPRISE: { limits: ENTERPRISE.limits, price: ENTERPRISE.price } });
}

runExample();
