
# Mẫu Prototype (Python)

## Cấu trúc
- `Structure/`: Các lớp cốt lõi cho mẫu Prototype
  - `prototype.py`: Interface Prototype, ConcretePrototype, Client
  - `main.py`: Demo clone (nông vs sâu), so sánh tham chiếu và giá trị
- `Example/`: Ví dụ thực tế
  - `document_prototype.py`: Ví dụ clone đối tượng tài liệu
  - `main.py`: Demo clone nhiều biến thể từ prototype gốc

## Cách chạy

### Demo Structure
```bash
cd Creational/Prototype/Python/Structure
python main.py
```

**Kết quả mẫu:**
```
Original id: ...
Shallow clone id: ...
Deep clone id: ...
Original nested id: ...
Shallow clone nested id: ...
Deep clone nested id: ...
--- Modifying shallow clone nested data ---
Original nested data: 99
Shallow clone nested data: 99
Deep clone nested data: 42
```

### Demo Example
```bash
cd Creational/Prototype/Python/Example
python main.py
```


**Kết quả mẫu:**
```
Base Doc: Something ['heheh', 'gegege', 'variant1']
Variant 1: Variant 1 ['heheh', 'gegege', 'variant1']
Variant 2: Variant 2 ['heheh', 'gegege', 'variant2']
```

## Giải thích cấu trúc
- Interface Prototype định nghĩa phương thức `clone()`
- ConcretePrototype triển khai clone (nông/sâu)
- Client sử dụng prototype để tạo bản sao
- Example minh hoạ ứng dụng thực tế (biến thể tài liệu)

## Sử dụng
- Dùng `Structure/` để học về mẫu Prototype
- Dùng `Example/` cho ứng dụng thực tế

---
