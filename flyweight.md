# Flyweight Pattern Demo – Cờ Tướng (Chinese Chess)

## 1. Ý tưởng áp dụng Flyweight
Trong cờ tướng có **32 quân**, nhưng thực tế chỉ có **7 loại quân** (Tướng, Sĩ, Tượng, Xe, Pháo, Mã, Tốt).  

- Các quân cùng loại có **hình dạng / hành vi giống nhau**, chỉ khác:  
  - **Màu sắc** (Đỏ/Đen)  
  - **Tọa độ trên bàn cờ**  

➡️ Nếu tạo 1 object riêng cho từng quân sẽ tốn bộ nhớ.  
➡️ Dùng **Flyweight**:  
- **Intrinsic state (nội tại – dùng chung):** loại quân, màu, cách di chuyển.  
- **Extrinsic state (ngoại tại – không dùng chung):** vị trí hiện tại (x, y).  

---

## 2. UML minh họa

Flyweight (Piece)

render(x, y)

ConcreteFlyweight (ConcretePiece)

type: String

color: String

render(x, y)

FlyweightFactory (PieceFactory)

pool: Map<String, Piece>

Client (ChessGame)



---

## 3. Code Demo (Java)

```java
import java.util.HashMap;
import java.util.Map;

// Flyweight interface
interface Piece {
    void render(int x, int y);
}

// ConcreteFlyweight
class ConcretePiece implements Piece {
    private final String type;   // intrinsic
    private final String color;  // intrinsic

    public ConcretePiece(String type, String color) {
        this.type = type;
        this.color = color;
    }

    @Override
    public void render(int x, int y) {
        System.out.println(color + " " + type + " ở vị trí (" + x + "," + y + ")");
    }
}

// Flyweight Factory
class PieceFactory {
    private static final Map<String, Piece> pool = new HashMap<>();

    public static Piece getPiece(String type, String color) {
        String key = type + "-" + color;
        if (!pool.containsKey(key)) {
            pool.put(key, new ConcretePiece(type, color));
            System.out.println("Tạo mới quân: " + key);
        }
        return pool.get(key);
    }
}

// Client
public class ChessGame {
    public static void main(String[] args) {
        // Lấy các quân từ factory
        Piece redXe = PieceFactory.getPiece("Xe", "Đỏ");
        Piece blackXe = PieceFactory.getPiece("Xe", "Đen");

        // Dùng chung object, chỉ khác extrinsic state (vị trí)
        redXe.render(0, 0);
        redXe.render(8, 0);

        blackXe.render(0, 9);
        blackXe.render(8, 9);

        // Lấy lại sẽ không tạo mới, dùng lại từ pool
        Piece redXe2 = PieceFactory.getPiece("Xe", "Đỏ");
        System.out.println("redXe == redXe2 ? " + (redXe == redXe2));
    }
}

4. Output khi chạy

Tạo mới quân: Xe-Đỏ
Tạo mới quân: Xe-Đen
Đỏ Xe ở vị trí (0,0)
Đỏ Xe ở vị trí (8,0)
Đen Xe ở vị trí (0,9)
Đen Xe ở vị trí (8,9)
redXe == redXe2 ? true
