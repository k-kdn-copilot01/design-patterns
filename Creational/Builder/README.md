# Builder Pattern in Python

**Builder** là mẫu thiết kế khởi tạo giúp tách biệt quá trình xây dựng một đối tượng phức tạp khỏi biểu diễn cuối cùng của nó. Director chịu trách nhiệm gọi tuần tự các bước xây dựng, có thể thay đổi Builder để tạo ra các biến thể khác nhau của cùng một Product.

---

## 📁 Folder Structure

### Structure
```
Creational/Builder/Python/Structure/
├── product.py         # Product class
├── builder.py         # Builder interface + ConcreteBuilders
├── director.py        # Director orchestrates building
└── main.py            # Demo
```

### Example
```
Creational/Builder/Python/Example/
├── meal.py            # Product: Meal
├── meal_builder.py    # Builders for Veg/NonVeg
├── director.py        # MealDirector
└── main.py            # Demo
```

---

## 🚀 Run Demos

### 1. Structure Demo
```bash
cd Creational/Builder/Python/Structure
python main.py
```
**Expected Output:**
```
Product parts: PartA1, PartB1
Product parts: PartA2, PartB2
```

### 2. Example Demo
```bash
cd Creational/Builder/Python/Example
python main.py
```
**Expected Output:**
```
Meal includes: Juice, Veg Burger, Fruit Salad
Meal includes: Coke, Chicken Burger, Ice Cream
```

---

## 🎯 Key Idea

- **Builder** tách quá trình xây dựng một object phức tạp khỏi biểu diễn cuối cùng.
- **Director** chịu trách nhiệm gọi tuần tự các bước xây dựng.
- Có thể thay đổi Builder để tạo ra biến thể khác nhau của cùng một Product.

---

## 📚 Reference

- [Refactoring.Guru – Builder](https://refactoring.guru/design-patterns/builder)
- [README gốc](../../README.md)

---

## 📜 License

MIT License. Xem chi tiết tại [LICENSE](../../LICENSE).