# Factory Method Design Pattern

**Factory Method** là một trong những mẫu thiết kế khởi tạo (Creational Pattern) giúp tách biệt quá trình tạo đối tượng khỏi logic sử dụng đối tượng, cho phép mở rộng linh hoạt các loại sản phẩm mà không cần thay đổi client code.

---

## 📁 Folder Structure

```
Creational/
└── FactoryMethod/
    ├── <Language>/
    │   ├── Structure/
    │   │   ├── product.*
    │   │   ├── concrete_product_a.*
    │   │   ├── concrete_product_b.*
    │   │   ├── creator.*
    │   │   ├── concrete_creator_a.*
    │   │   ├── concrete_creator_b.*
    │   │   ├── client.*
    │   │   └── main.*
    │   └── Example/
    │       ├── transport.*
    │       ├── truck.*
    │       ├── ship.*
    │       ├── logistics.*
    │       ├── road_logistics.*
    │       ├── sea_logistics.*
    │       ├── client.*
    │       └── main.*
    └── README.md
```

- **Structure/**: Cài đặt core pattern (Product, Creator, ConcreteProduct, ConcreteCreator, Client, Main)
- **Example/**: Ví dụ thực tế (Logistics: RoadLogistics, SeaLogistics, Truck, Ship, Main)

---

## 🚀 How to Run

### 1. Structure Demo (Kiểm thử cấu trúc Factory Method)

**Python:**
```bash
cd Creational/FactoryMethod/Structure
python main.py
```

### 2. Example Demo (Kịch bản thực tế)

**Python:**
```bash
cd Creational/FactoryMethod/Example
python main.py
```

---

## 📊 Expected Output

### Structure Demo

```
App: Using ConcreteCreatorA
Creator: working with Result of ConcreteProductA

App: Using ConcreteCreatorB
Creator: working with Result of ConcreteProductB
```

### Example Demo

```
App: Using RoadLogistics
Client: Planning delivery...
Deliver by land in a truck

App: Using SeaLogistics
Client: Planning delivery...
Deliver by sea in a ship
```

---

## 🎯 Key Concepts

- **Factory Method**: Định nghĩa interface cho việc tạo đối tượng, cho phép subclass quyết định loại đối tượng sẽ tạo.
- **Creator**: Lớp cơ sở định nghĩa factory method.
- **ConcreteCreator**: Cài đặt factory method để trả về sản phẩm cụ thể.
- **Product**: Interface hoặc lớp cơ sở cho các sản phẩm.
- **ConcreteProduct**: Các loại sản phẩm cụ thể.

---

## 🔍 Best Practices

- Sử dụng Factory Method khi cần mở rộng loại sản phẩm mà không thay đổi client code.
- Tách biệt logic khởi tạo khỏi logic sử dụng.
- Dễ dàng mở rộng, bảo trì và kiểm thử.

---

## 📚 Reference

- [Refactoring.Guru – Factory Method](https://refactoring.guru/design-patterns/factory-method)
- [README gốc](../../README.md)

---

## 🤝 Contribution

- Thêm ví dụ cho các ngôn ngữ khác (Java, PHP, ...)
- Đóng góp thêm các kịch bản thực tế
- Cải thiện chất lượng code và tài liệu

---

## 📜 License

MIT License. Xem chi tiết tại [LICENSE](../../LICENSE).