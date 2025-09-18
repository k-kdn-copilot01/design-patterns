# Factory Method Design Pattern - Java Implementation

This folder contains Java implementations of the **Factory Method** design pattern, demonstrating both structural components and a real-world football game example.

## 📁 Folder Structure

- `Structure/`
  - `Product.java` — Interface chung cho tất cả products
  - `ConcreteProductA.java` — Implementation cụ thể của Product A
  - `ConcreteProductB.java` — Implementation cụ thể của Product B
  - `Creator.java` — Abstract class định nghĩa factory method
  - `ConcreteCreatorA.java` — Creator tạo Product A
  - `ConcreteCreatorB.java` — Creator tạo Product B
  - `Main.java` — Demo cho structure-only implementations
- `Example/`
  - `Player.java` — Interface cho cầu thủ trong game đá bóng
  - `Striker.java`, `Midfielder.java`, `Defender.java` — Các loại cầu thủ
  - `TeamManager.java` — Abstract class cho huấn luyện viên
  - `AttackingManager.java`, `DefensiveManager.java`, `BalancedManager.java` — Các kiểu HLV
  - `Main.java` — Demo với ví dụ thực tế
- `README.md` — Tài liệu này

## 🎯 Khi nào sử dụng Factory Method

Factory Method pattern nên được sử dụng khi:
- Bạn không biết trước chính xác loại và dependencies của objects mà code cần làm việc
- Bạn muốn cung cấp cho users khả năng extend internal components
- Bạn muốn tái sử dụng existing objects thay vì rebuild chúng mỗi lần
- Bạn muốn de-couple code khỏi concrete classes

## 🏗️ Cấu trúc Pattern

### Core Components:

1. **Product Interface** (`Product.java`)
   - Định nghĩa interface chung cho tất cả objects mà factory method có thể tạo

2. **Concrete Products** (`ConcreteProductA.java`, `ConcreteProductB.java`)
   - Implementations khác nhau của Product interface

3. **Creator Abstract Class** (`Creator.java`)
   - Khai báo factory method trả về Product object
   - Có thể chứa business logic sử dụng Product

4. **Concrete Creators** (`ConcreteCreatorA.java`, `ConcreteCreatorB.java`)
   - Override factory method để return specific concrete product

## ⚽ Real-World Example: Football Game

Ví dụ này mô phỏng một game đá bóng với các HLV khác nhau:

### Strategy Differences:

- **AttackingManager**: Tạo Striker → Chiến thuật tấn công (4-2-4)
- **DefensiveManager**: Tạo Defender → Chiến thuật phòng thủ (5-4-1)  
- **BalancedManager**: Tạo Midfielder → Chiến thuật cân bằng (4-4-2)

## 🚀 Cách chạy

1. **Demo structure implementations:**
   ```bash
   cd Creational/FactoryMethod/Java/Structure
   javac *.java
   java Main
   ```

2. **Demo football game example:**
   ```bash
   cd Creational/FactoryMethod/Java/Example
   javac *.java
   java Main
   ```

## 📊 Expected Output (Structure/Main)

```
=== Demo Cấu Trúc: Factory Method Pattern ===

1. Sử dụng ConcreteCreatorA:
Client: Làm việc với creator (không biết concrete class)
Creator: Bắt đầu thực hiện nghiệp vụ...
ConcreteCreatorA: Tạo Product A
Creator: Đang làm việc với Sản phẩm A
ConcreteProductA đang thực hiện thao tác
Creator: Hoàn thành thực hiện nghiệp vụ.

2. Sử dụng ConcreteCreatorB:
Client: Làm việc với creator (không biết concrete class)
Creator: Bắt đầu thực hiện nghiệp vụ...
ConcreteCreatorB: Tạo Product B
Creator: Đang làm việc với Sản phẩm B
ConcreteProductB đang thực hiện thao tác
Creator: Hoàn thành thực hiện nghiệp vụ.

3. Minh họa tính đa hình:
Creator 1:
Creator: Bắt đầu thực hiện nghiệp vụ...
ConcreteCreatorA: Tạo Product A
Creator: Đang làm việc với Sản phẩm A
ConcreteProductA đang thực hiện thao tác
Creator: Hoàn thành thực hiện nghiệp vụ.

Creator 2:
Creator: Bắt đầu thực hiện nghiệp vụ...
ConcreteCreatorB: Tạo Product B
Creator: Đang làm việc với Sản phẩm B
ConcreteProductB đang thực hiện thao tác
Creator: Hoàn thành thực hiện nghiệp vụ.

=== Hoàn Thành Demo Cấu Trúc ===
```

## 📊 Expected Output (Example/Main)

```
=== Demo Ví Dụ: Game Đá Bóng Factory Method ===

🏆 MÔ PHỌNG TRẬN ĐẤU ĐÁ BÓNG 🏆

=== Team A (Attacking) ===
AttackingManager: Thực hiện chiến thuật ép sân!
Sơ đồ: 4-2-4 (Tập trung ghi bàn)

Manager: Đang thiết lập đội hình...
AttackingManager: Cầu thủ tấn công - Ronaldo
Manager: Ronaldo được phân công vào vị trí Tiền đạo
Ronaldo (Tiền đạo) đang tấn công và tìm kiếm cơ hội ghi bàn
Ronaldo thực hiện sút mạnh vào khung thành!

AttackingManager: Cầu thủ tấn công - Messi
Manager: Messi được phân công vào vị trí Tiền đạo
Messi (Tiền đạo) đang tấn công và tìm kiếm cơ hội ghi bàn
Messi thực hiện sút mạnh vào khung thành!

AttackingManager: Cầu thủ tấn công - Neymar
Manager: Neymar được phân công vào vị trí Tiền đạo
Neymar (Tiền đạo) đang tấn công và tìm kiếm cơ hội ghi bàn
Neymar thực hiện sút mạnh vào khung thành!

Manager: Hoàn thành thiết lập đội hình!
Hoàn thành mô phỏng trận đấu cho Team A (Attacking)!

──────────────────────────────────────────────────

=== Team B (Defensive) ===
DefensiveManager: Thực hiện chiến thuật phòng thủ đổ bê tông!
Sơ đồ: 5-4-1 (Tập trung ngăn chặn bàn thắng)

Manager: Đang thiết lập đội hình...
DefensiveManager: Cầu thủ phòng thủ - Ramos
Manager: Ramos được phân công vào vị trí Hậu vệ
Ramos (Hậu vệ) đang bảo vệ khung thành và ngăn chặn các cuộc tấn công
Ramos thực hiện pha cướp bóng quan trọng và giải tòa!

DefensiveManager: Cầu thủ phòng thủ - Pique
Manager: Pique được phân công vào vị trí Hậu vệ
Pique (Hậu vệ) đang bảo vệ khung thành và ngăn chặn các cuộc tấn công
Pique thực hiện pha cướp bóng quan trọng và giải tòa!

DefensiveManager: Cầu thủ phòng thủ - Maldini
Manager: Maldini được phân công vào vị trí Hậu vệ
Maldini (Hậu vệ) đang bảo vệ khung thành và ngăn chặn các cuộc tấn công
Maldini thực hiện pha cướp bóng quan trọng và giải tòa!

Manager: Hoàn thành thiết lập đội hình!
Hoàn thành mô phỏng trận đấu cho Team B (Defensive)!

──────────────────────────────────────────────────

=== Team C (Balanced) ===
BalancedManager: Thực hiện chiến thuật phòng ngự phản công!
Sơ đồ: 4-4-2 (Vừa tấn công và phòng thủ)

Manager: Đang thiết lập đội hình...
BalancedManager: Cầu thủ tiền vệ - Modric
Manager: Modric được phân công vào vị trí Tiền vệ
Modric (Tiền vệ) đang kiểm soát lối chơi và phân phối bóng
Modric thực hiện đường chọc khe như sách giáo khoa cho tiền đạo!

BalancedManager: Cầu thủ tiền vệ - Iniesta
Manager: Iniesta được phân công vào vị trí Tiền vệ
Iniesta (Tiền vệ) đang kiểm soát lối chơi và phân phối bóng
Iniesta thực hiện đường chọc khe như sách giáo khoa cho tiền đạo!

BalancedManager: Cầu thủ tiền vệ - Pirlo
Manager: Pirlo được phân công vào vị trí Tiền vệ
Pirlo (Tiền vệ) đang kiểm soát lối chơi và phân phối bóng
Pirlo thực hiện đường chọc khe như sách giáo khoa cho tiền đạo!

Manager: Hoàn thành thiết lập đội hình!
Hoàn thành mô phỏng trận đấu cho Team C (Balanced)!

──────────────────────────────────────────────────

🔄 MINH HỌA TÍNH LINH HOẠT CỦA HUẤN LUYỆN VIÊN:

Cách tiếp cận của HLV 1:
Manager: Đang thiết lập đội hình...
AttackingManager: Cầu thủ tấn công - Cristiano Ronaldo
Manager: Cristiano Ronaldo được phân công vào vị trí Tiền đạo
Cristiano Ronaldo (Tiền đạo) đang tấn công và tìm kiếm cơ hội ghi bàn
Cristiano Ronaldo thực hiện sút mạnh vào khung thành!

Manager: Hoàn thành thiết lập đội hình!
Cách tiếp cận của HLV 2:
Manager: Đang thiết lập đội hình...
DefensiveManager: Cầu thủ phòng thủ - Cristiano Ronaldo
Manager: Cristiano Ronaldo được phân công vào vị trí Hậu vệ
Cristiano Ronaldo (Hậu vệ) đang bảo vệ khung thành và ngăn chặn các cuộc tấn công
Cristiano Ronaldo thực hiện pha cướp bóng quan trọng và giải tòa!

Manager: Hoàn thành thiết lập đội hình!
Cách tiếp cận của HLV 3:
Manager: Đang thiết lập đội hình...
BalancedManager: Cầu thủ tiền vệ - Cristiano Ronaldo
Manager: Cristiano Ronaldo được phân công vào vị trí Tiền vệ
Cristiano Ronaldo (Tiền vệ) đang kiểm soát lối chơi và phân phối bóng
Cristiano Ronaldo thực hiện đường chọc khe như sách giáo khoa cho tiền đạo!

Manager: Hoàn thành thiết lập đội hình!
=== Hoàn Thành Demo Ví Dụ ===
```
