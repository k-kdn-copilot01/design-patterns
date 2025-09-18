# Abstract Factory Pattern in Python

**Abstract Factory** là mẫu thiết kế khởi tạo cho phép tạo ra một họ các đối tượng liên quan hoặc phụ thuộc mà không cần chỉ rõ lớp cụ thể của chúng. Client chỉ làm việc với interface, giúp dễ dàng thay đổi họ sản phẩm.

---

## 📁 Folder Structure

### Structure
```
Creational/AbstractFactory/Python/Structure/
├── abstract_product.py      # Abstract products (A, B)
├── concrete_products.py     # Concrete products (A1, A2, B1, B2)
├── abstract_factory.py      # Abstract factory
├── concrete_factories.py    # Concrete factories
├── client.py                # Client
└── main.py                  # Demo
```

### Example
```
Creational/AbstractFactory/Python/Example/
├── gui_factory.py           # Abstract factory & abstract products
├── windows_factory.py       # Windows concrete factory + products
├── mac_factory.py           # Mac concrete factory + products
├── client.py                # Application uses factory
└── main.py                  # Demo
```

---

## 🚀 Run Demos

### 1. Structure Demo
```bash
cd Creational/AbstractFactory/Python/Structure
python main.py
```
**Expected Output:**
```
ProductA1 + ProductB1
ProductA2 + ProductB2
```

### 2. Example Demo
```bash
cd Creational/AbstractFactory/Python/Example
python main.py
```
**Expected Output:**
```
Using Windows Factory:
Render a button in Windows style
Render a checkbox in Windows style

Using Mac Factory:
Render a button in Mac style
Render a checkbox in Mac style
```

---

## 🎯 Key Idea

- **Abstract Factory** cung cấp interface để tạo ra một họ các đối tượng liên quan mà không cần chỉ rõ lớp cụ thể.
- Client chỉ làm việc với interface, giúp dễ dàng thay đổi họ sản phẩm.

---

## 📚 Reference

- [Refactoring.Guru – Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)
- [README gốc](../../README.md)

---

## 📜 License

MIT License. Xem chi tiết tại [LICENSE](../../LICENSE).