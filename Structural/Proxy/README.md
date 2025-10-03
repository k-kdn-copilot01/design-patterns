# Proxy Pattern – Ví dụ Truy cập Video

## 🎯 Mục tiêu
- **Proxy Pattern** cung cấp một lớp thay thế (proxy) để kiểm soát quyền truy cập tới một đối tượng thật (RealSubject).
- Proxy thường dùng để:
  - **Lazy Loading**: trì hoãn việc khởi tạo đối tượng nặng cho đến khi thực sự cần.
  - **Access Control**: kiểm soát quyền truy cập (ví dụ: check quyền user).
  - **Logging / Caching**: thêm logic phụ trợ.

---
