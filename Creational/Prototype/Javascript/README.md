# Prototype Pattern — JavaScript

- `Structure/`: minh hoạ core classes (Prototype, ConcretePrototype, Client) + demo shallow vs deep clone.
- `Example/`: kịch bản thực tế — clone nhanh nhiều biến thể cấu hình sản phẩm từ prototype gốc.

## Cấu trúc thư mục
```text
Creational/Prototype/JavaScript/
├── README.md
├── Structure/
│   ├── Prototype.js
│   ├── ConcretePrototype.js
│   ├── Client.js
│   ├── Main.js
│   └── utils.js
└── Example/
    ├── ProductConfigPrototype.js
    └── Main.js
```

## Cách chạy
Yêu cầu Node.js (>= 14). Khuyến nghị Node 18+ để có `structuredClone`.

Chạy từng phần trực tiếp bằng `node`:
```bash
node JavaScript/Structure/Main.js
node JavaScript/Example/Main.js
```

Hoặc dùng `npm` script (nếu đặt `package.json` ở gốc repo):
```jsonc
{
  "scripts": {
    "prototype:structure": "node JavaScript/Structure/Main.js",
    "prototype:example":   "node JavaScript/Example/Main.js"
  }
}
```

## Expected Output (Structure)
Ví dụ rút gọn (thực tế sẽ in thêm mảng/tài liệu):
```text
Top-level identity:
original === shallow ? false
original === deep    ? false

Nested reference equality (before mutation):
original.meta === shallow.meta ? true
original.meta === deep.meta    ? false

After mutation:
original.meta.author.name => Bob
deep.meta.pages            => 200
original.meta.pages        => 120

Arrays:
original.tags => [ 'patterns', 'oop', 'shallow-edit' ]
deep.tags     => [ 'patterns', 'oop', 'deep-edit' ]

Array reference equality:
original.tags === shallow.tags ? true
original.tags === deep.tags    ? false
```

## Expected Output (Example)
```text
Identity checks:
base === FREE ? false
base === PRO  ? false
base === ENT  ? false

FREE.features.ai.moderation.vendor => LiteVendor
base.features.ai.moderation.vendor  => OpenAI

PRO.limits.users       => 12345
ENTERPRISE.limits.users => 100000
```