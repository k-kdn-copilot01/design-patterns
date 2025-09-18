# Factory Method Pattern

## 📖 Mô tả (Description)

Factory Method là một creational design pattern cung cấp interface để tạo objects trong superclass, nhưng cho phép subclasses thay đổi loại objects được tạo ra.

**Vấn đề giải quyết:**
- Tạo objects mà không cần specify exact class của chúng
- Tách rời logic tạo object khỏi business logic
- Cho phép mở rộng dễ dàng khi cần thêm loại objects mới

**Ưu điểm:**
- ✅ Tránh tight coupling giữa creator và concrete products
- ✅ Tuân thủ Single Responsibility Principle
- ✅ Tuân thủ Open/Closed Principle
- ✅ Dễ dàng mở rộng với product types mới

**Nhược điểm:**
- ❌ Code có thể trở nên phức tạp vì cần nhiều subclasses

## 🏗️ Cấu trúc (Structure)

```
Product (Interface/Abstract)
├── ConcreteProductA
└── ConcreteProductB

Creator (Abstract)
├── ConcreteCreatorA → tạo ConcreteProductA  
└── ConcreteCreatorB → tạo ConcreteProductB

Client → sử dụng Creator interface
```

### Thành phần chính:

1. **Product**: Interface chung cho tất cả objects được tạo bởi creator
2. **ConcreteProduct**: Các implementation khác nhau của Product interface
3. **Creator**: Class khai báo factory method trả về Product objects
4. **ConcreteCreator**: Override factory method để trả về instance của ConcreteProduct

## 📁 Cấu trúc thư mục

```
FactoryMethod/
├── Python/
│   ├── Structure/          # Cấu trúc chuẩn pattern
│   │   ├── product.py
│   │   ├── concrete_products.py
│   │   ├── creator.py
│   │   ├── concrete_creators.py
│   │   ├── client.py
│   │   └── main.py
│   │
│   └── Example/           # Ví dụ thực tế - Logistics
│       ├── transport.py
│       ├── vehicles.py
│       ├── logistics.py
│       ├── logistics_manager.py
│       └── main.py
│
└── README.md
```

## 🚀 Cách chạy (How to Run)

### Structure Demo (Cấu trúc chuẩn)

```bash
cd Python/Structure
python main.py
```

### Example Demo (Ví dụ Logistics)

```bash
cd Python/Example  
python main.py
```

## 📋 Expected Output

### Structure Demo Output:

```
Factory Method Pattern - Structure Demo
==================================================

1. Working with ConcreteCreatorA:
Client: I'm not aware of the creator's class, but it still works.
Creator: Working with Result of ConcreteProductA operation

------------------------------

2. Working with ConcreteCreatorB:
Client: I'm not aware of the creator's class, but it still works.
Creator: Working with Result of ConcreteProductB operation

==================================================
Demo completed successfully!
```

### Example Demo Output:

```
🏭 Factory Method Pattern - Logistics Example
============================================================

📍 Scenario 1: Domestic Delivery (Short Distance)
---------------------------------------------
🚚 Planning delivery to: Hanoi to Ho Chi Minh City
📋 Logistics Planning:
- Truck capacity: 10-30 tons, suitable for medium-distance land transport
- Delivering by land in a box via truck
✅ Delivery planned successfully!

📍 Scenario 2: International Delivery (Overseas)
---------------------------------------------
🚚 Planning delivery to: Vietnam to United States
📋 Logistics Planning:
- Ship capacity: 1000-10000 tons, suitable for long-distance overseas transport
- Delivering by sea in a container via ship
✅ Delivery planned successfully!

📍 Scenario 3: Express International Delivery
---------------------------------------------
🚚 Planning delivery to: Vietnam to Japan
📋 Logistics Planning:
- Airplane capacity: 5-50 tons, suitable for fast international delivery
- Delivering by air in a cargo hold via airplane
✅ Delivery planned successfully!

📍 Scenario 4: Logistics Comparison
------------------------------
🔍 Comparing logistics options for delivery to: Vietnam to Europe
============================================================

Option 1: RoadLogistics
------------------------------
📦 Truck capacity: 10-30 tons, suitable for medium-distance land transport
🚛 Delivering by land in a box via truck

Option 2: SeaLogistics
------------------------------
📦 Ship capacity: 1000-10000 tons, suitable for long-distance overseas transport
🚛 Delivering by sea in a container via ship

Option 3: AirLogistics
------------------------------
📦 Airplane capacity: 5-50 tons, suitable for fast international delivery
🚛 Delivering by air in a cargo hold via airplane

============================================================

🎉 Factory Method Pattern demonstration completed!
📝 Notice how each logistics type creates different transport vehicles
   without the client code knowing the specific implementation details.
```

## 💡 Khi nào sử dụng (When to Use)

1. **Khi bạn không biết trước loại objects cần tạo**: Pattern giúp tách rời code tạo objects khỏi code sử dụng chúng

2. **Khi muốn cung cấp cho users một cách để extend internal components**: Users có thể extend app thông qua inheritance

3. **Khi muốn tiết kiệm system resources**: Reuse existing objects thay vì rebuild chúng mỗi lần

4. **Khi cần flexibility trong việc chọn products**: Runtime decision về loại product cần tạo

## 🔄 So sánh với patterns khác

| Pattern | Mục đích | Khi nào dùng |
|---------|----------|--------------|
| **Factory Method** | Tạo objects thông qua inheritance | Khi cần subclasses quyết định loại object |
| **Abstract Factory** | Tạo families của objects | Khi cần tạo nhiều related objects |
| **Builder** | Construct complex objects step by step | Khi object có nhiều optional parameters |
| **Prototype** | Clone existing objects | Khi việc tạo object rất expensive |

## 📚 Tài liệu tham khảo

- [Refactoring Guru - Factory Method](https://refactoring.guru/design-patterns/factory-method)
- [Gang of Four Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns)

---

*Factory Method Pattern implementation với Python - Học thiết kế hướng đối tượng qua ví dụ thực tế*
