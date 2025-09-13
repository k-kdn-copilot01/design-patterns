# Prototype Design Pattern

## Mô tả (Description)

Prototype là một mẫu thiết kế sáng tạo (Creational Design Pattern) cho phép tạo ra các đối tượng mới bằng cách sao chép (clone) từ một đối tượng mẫu có sẵn, thay vì tạo mới từ đầu. Pattern này đặc biệt hữu ích khi việc tạo đối tượng mới tốn kém về mặt tài nguyên hoặc phức tạp.

**Prototype** is a creational design pattern that allows creating new objects by cloning existing prototype objects instead of creating them from scratch. This pattern is particularly useful when object creation is expensive or complex.

## Cấu trúc (Structure)

### Thành phần chính:

1. **Prototype Interface**: Định nghĩa phương thức clone()
2. **ConcretePrototype**: Triển khai phương thức clone() cụ thể
3. **Client**: Sử dụng prototype để tạo đối tượng mới

### Sơ đồ cấu trúc:
```
┌─────────────────┐
│   <<interface>> │
│    Prototype    │
│                 │
│ + clone()       │
└─────────────────┘
         ▲
         │ implements
         │
┌─────────────────┐     ┌─────────────────┐
│ ConcreteProto-  │     │     Client      │
│    type A       │────▶│                 │
│                 │     │ - prototype     │
│ + clone()       │     │ + operation()   │
└─────────────────┘     └─────────────────┘
```

## Cách chạy (How to Run)

### Yêu cầu hệ thống:
- Python 3.7+
- Không cần thư viện bên ngoài

### 1. Structure Demo - Minh họa cấu trúc cơ bản

```bash
cd Creational/Prototype/Python/Structure/
python main.py
```

**Chức năng Structure Demo:**
- Minh họa shallow clone vs deep clone
- Thể hiện sự độc lập giữa các đối tượng
- Quản lý prototype thông qua Client
- So sánh object identity và memory addresses

### 2. Example Demo - Ví dụ thực tế

```bash
cd Creational/Prototype/Python/Example/
python main.py
```

**Chức năng Example Demo:**
- Hệ thống quản lý tài liệu
- Template-based document generation
- Contract và Report template cloning
- Document Manager với prototype registry
- Performance comparison

## Kết quả mong đợi (Expected Output)

### Structure Demo Output:
```
PROTOTYPE PATTERN - STRUCTURE DEMONSTRATION
Showcasing clone functionality and object independence

============================================================
SHALLOW vs DEEP CLONE DEMONSTRATION
============================================================
Original: ConcretePrototypeA(id=..., value='Original', data=['item1', 'item2'])
Shallow Clone: ConcretePrototypeA(id=..., value='Original', data=['item1', 'item2'])
Deep Clone: ConcretePrototypeA(id=..., value='Original', data=['item1', 'item2'])

--- Testing Reference vs Value ---

Modifying original data...
Original after modification: ConcretePrototypeA(id=..., value='Modified Original', data=['item1', 'item2', 'item3'])
Shallow Clone after original modification: ConcretePrototypeA(id=..., value='Original', data=['item1', 'item2', 'item3'])
Deep Clone after original modification: ConcretePrototypeA(id=..., value='Original', data=['item1', 'item2'])

Note: Shallow clone shares the 'data' list with original!
      Deep clone has independent copy of all data.

============================================================
CLIENT PROTOTYPE MANAGEMENT
============================================================
Registered prototypes:
typeA: ConcretePrototypeA(id=..., value='Template A', data=['default'])
typeB: ConcretePrototypeB(id=..., name='Template B', config={'theme': 'dark', 'lang': 'en'})

--- Creating clones via Client ---
Clone A1: ConcretePrototypeA(id=..., value='Template A', data=['default'])
Clone A2: ConcretePrototypeA(id=..., value='Template A', data=['default'])
Clone B1: ConcretePrototypeB(id=..., name='Template B', config={'theme': 'dark', 'lang': 'en'})

============================================================
OBJECT IDENTITY DEMONSTRATION
============================================================
Original ID: ... | Object: ConcretePrototypeA(id=..., value='Identity Test', data=['shared'])
Clone ID: ... | Object: ConcretePrototypeA(id=..., value='Identity Test', data=['shared'])
Deep Clone ID: ... | Object: ConcretePrototypeA(id=..., value='Identity Test', data=['shared'])

Are objects the same? Original == Clone: False
Are data lists the same? Original.data == Clone.data: True
Are data lists the same? Original.data == DeepClone.data: False
```

### Example Demo Output:
```
PROTOTYPE PATTERN - REAL-WORLD EXAMPLE
Document Management System
Demonstrating practical application of the Prototype pattern

======================================================================
BASIC DOCUMENT CLONING DEMONSTRATION
======================================================================
Original: Document: 'Project Proposal Template' (v1, 44 chars)
Content length: 44 characters
Tags: ['template', 'proposal']
Attachments: 1

Cloned: Document: 'AI Project Proposal' (v2, 56 chars)
Content length: 56 characters
Tags: ['template', 'proposal', 'AI']
Attachments: 1

After adding attachment to original:
Original attachments: 2
Cloned attachments: 1
Note: Deep clone maintains independence!

======================================================================
REPORT TEMPLATE SYSTEM DEMONSTRATION
======================================================================
Master Template: Report: 'Quarterly Business Report' (quarterly, 6 sections, 2 charts)
Charts: 2

Q1 Report: Report: 'Q1 2024 Business Report' (quarterly, 6 sections, 3 charts)
Q2 Report: Report: 'Q2 2024 Business Report' (quarterly, 6 sections, 2 charts)

Master template sections: 6
Q1 charts: 3
Q2 charts: 2

======================================================================
DOCUMENT MANAGER DEMONSTRATION
======================================================================
Creating and registering templates...
Template 'basic' registered: Document: 'Standard Document Template' (v1, 82 chars)
Template 'monthly_report' registered: Report: 'Monthly Report Template' (monthly, 6 sections, 1 charts)
Template 'nda' registered: Contract: 'Non-Disclosure Agreement' (nda, 1 terms, 1 clauses)

Available Templates:
----------------------------------------
- basic: Document: 'Standard Document Template' (v1, 82 chars)
- monthly_report: Report: 'Monthly Report Template' (monthly, 6 sections, 1 charts)
- nda: Contract: 'Non-Disclosure Agreement' (nda, 1 terms, 1 clauses)

========================================
Creating documents from templates...
========================================

Created Documents:
----------------------------------------
1. Document: 'User Manual v2.0' (v2, 67 chars)
   Created: 2024-xx-xx xx:xx
   Tags: standard, template, manual

2. Report: 'January 2024 Sales Report' (monthly, 6 sections, 1 charts)
   Created: 2024-xx-xx xx:xx
   Tags: report, monthly

3. Contract: 'Partnership NDA - TechCorp' (nda, 1 terms, 1 clauses)
   Created: 2024-xx-xx xx:xx
   Tags: contract, nda, legal
```

## Ưu điểm (Advantages)

1. **Hiệu suất cao**: Tạo đối tượng nhanh hơn so với khởi tạo từ đầu
2. **Giảm phức tạp**: Tránh việc khởi tạo phức tạp
3. **Linh hoạt**: Có thể tạo nhiều biến thể từ một prototype
4. **Độc lập**: Các bản sao độc lập với nhau (khi dùng deep clone)

## Nhược điểm (Disadvantages)

1. **Phức tạp với deep clone**: Xử lý circular references
2. **Quản lý bộ nhớ**: Cần chú ý shallow vs deep clone
3. **Dependency**: Các lớp phải implement clone method

## Khi nào sử dụng (When to Use)

- Khi việc tạo đối tượng tốn kém tài nguyên
- Khi cần tạo nhiều đối tượng tương tự
- Khi muốn tránh việc khởi tạo phức tạp
- Khi cần hệ thống template linh hoạt

## Các Pattern liên quan (Related Patterns)

- **Factory Method**: Prototype có thể thay thế Factory trong một số trường hợp
- **Abstract Factory**: Có thể kết hợp với Prototype để tạo family objects
- **Composite**: Prototype thường được sử dụng với Composite pattern

## Files trong dự án

### Structure/
- `prototype.py`: Các lớp cơ bản (Prototype, ConcretePrototype, Client)
- `main.py`: Demo minh họa cấu trúc và chức năng clone

### Example/
- `document_prototype.py`: Hệ thống quản lý tài liệu thực tế
- `main.py`: Demo ứng dụng thực tế với document templates
