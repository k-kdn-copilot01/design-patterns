# Flyweight Pattern (Mẫu thiết kế Flyweight)

## Mô tả
Flyweight Pattern là một mẫu thiết kế cấu trúc (Structural Pattern) được sử dụng để giảm thiểu việc sử dụng bộ nhớ khi làm việc với một số lượng lớn các đối tượng tương tự. Pattern này chia sẻ hiệu quả các phần dữ liệu chung giữa nhiều đối tượng thay vì lưu trữ tất cả dữ liệu trong mỗi đối tượng.

## Khái niệm chính

### Intrinsic State (Trạng thái nội tại)
- Dữ liệu được chia sẻ giữa nhiều đối tượng
- Không thay đổi và độc lập với ngữ cảnh
- Được lưu trữ trong flyweight object

### Extrinsic State (Trạng thái ngoại lai)
- Dữ liệu phụ thuộc vào ngữ cảnh và thay đổi
- Được truyền vào flyweight từ bên ngoài
- Không được lưu trữ trong flyweight

## Cấu trúc

### 1. Structure/
Chứa cài đặt cơ bản của Flyweight Pattern:
- `flyweight.py`: Định nghĩa Flyweight interface và concrete flyweight classes
- `main.py`: Demo cơ bản về cách sử dụng pattern

### 2. Example/
Chứa ví dụ thực tế về Text Editor:
- `character_flyweight.py`: Flyweight cho các ký tự trong text editor
- `text_editor.py`: Context class quản lý text và formatting
- `main.py`: Demo hoàn chỉnh về text editor

## Ưu điểm
- Giảm đáng kể việc sử dụng RAM khi có nhiều đối tượng tương tự
- Tăng hiệu suất khi số lượng đối tượng lớn
- Centralized control cho các đối tượng được chia sẻ

## Nhược điểm
- Code phức tạp hơn do phải tách biệt intrinsic và extrinsic state
- CPU overhead khi tính toán extrinsic state
- Khó debug do objects được chia sẻ

## Khi nào sử dụng
- Khi ứng dụng cần tạo ra số lượng lớn các đối tượng tương tự
- Khi chi phí lưu trữ cao do số lượng đối tượng
- Khi có thể tách được intrinsic và extrinsic state
- Khi extrinsic state có thể được tính toán hoặc truyền từ bên ngoài

## Chạy demo

### Structure demo:
```bash
cd Structure/
python main.py
```

### Example demo:
```bash
cd Example/
python main.py
```
