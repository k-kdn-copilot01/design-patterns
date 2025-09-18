# Prototype Pattern (Python)

## Overview
**Prototype** là một Creational Design Pattern cho phép bạn tạo đối tượng mới bằng cách **clone** (sao chép) một prototype có sẵn thay vì khởi tạo trực tiếp.  
Điều này hữu ích khi việc tạo mới phức tạp hoặc tốn chi phí, và bạn muốn dễ dàng nhân bản nhiều đối tượng tương tự nhưng độc lập.

---

## 📁 Folder Structure
```
Creational/Prototype/Python/
├── Structure/           # Core conceptual demo
│   ├── prototype.py
│   ├── concrete_prototype_a.py
│   ├── concrete_prototype_b.py
│   ├── client.py
│   └── main.py
└── Example/             # Real-world demo
    ├── document.py
    ├── client.py
    └── main.py
```

---

## 🚀 Run

### 1. Structure Demo
```bash
cd Creational/Prototype/Python/Structure
python main.py
```
**Expected Output:**
```
Original A: ConcretePrototypeA(field='Hello')
Copy A: ConcretePrototypeA(field='Hello')
Same reference? False

Original B: ConcretePrototypeB(number=42)
Copy B: ConcretePrototypeB(number=42)
Same reference? False
```

### 2. Example Demo
```bash
cd Creational/Prototype/Python/Example
python main.py
```
**Expected Output:**
```
Prototype: Document(title='Template', content='Base content')
Doc1: Document(title='Contract A', content='Custom content A')
Doc2: Document(title='Contract B', content='Custom content B')
```

---

## 🎯 Key Points

- Prototype định nghĩa interface clone.
- ConcretePrototypeA minh họa shallow copy (dùng `copy.copy`).
- ConcretePrototypeB minh họa deep copy (dùng `copy.deepcopy`).
- Client chỉ biết gọi clone mà không phụ thuộc vào constructor của sản phẩm.
- Khi thay đổi concrete prototype, kết quả clone thay đổi theo.

---

## 📚 References

- [Refactoring Guru – Prototype](https://refactoring.guru/design-patterns/prototype)
- GoF: Design Patterns: Elements of Reusable Object-Oriented Software