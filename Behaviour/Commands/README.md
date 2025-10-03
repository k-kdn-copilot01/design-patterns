# Command Pattern – Ví dụ Bộ điều khiển đèn

## 🎯 Mục tiêu
- **Command Pattern** đóng gói một yêu cầu thành một đối tượng (Command).  
- Giúp tách rời **người gọi hành động (Invoker)** và **người thực thi hành động (Receiver)**.  
- Cho phép:
  - Lưu trữ và log lại các lệnh
  - Hỗ trợ undo/redo
  - Hàng đợi command để xử lý sau

---