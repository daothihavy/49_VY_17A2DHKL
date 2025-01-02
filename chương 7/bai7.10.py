import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# Hàm xử lý khi nhấn nút "Gửi"
def submit_data():
    # Lấy tên và tuổi từ hộp thoại
    name = simpledialog.askstring("Nhập Tên", "Vui lòng nhập tên của bạn:")
    age = simpledialog.askinteger("Nhập Tuổi", "Vui lòng nhập tuổi của bạn:")

    if name and age is not None:  # Kiểm tra nếu người dùng đã nhập đầy đủ thông tin
        # Tạo thông báo
        greeting_message = f"Xin chào, {name}!"
        if age >= 18:
            age_message = f"Bạn đã trưởng thành! ({age} tuổi)"
        else:
            age_message = f"Bạn còn nhỏ tuổi! ({age} tuổi)"
        
        # Hiển thị thông báo
        messagebox.showinfo("Thông báo", f"{greeting_message}\n{age_message}")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Thông Tin Người Dùng")

# Tạo nút "Gửi" để thu thập thông tin
submit_button = tk.Button(window, text="Gửi", command=submit_data)
submit_button.pack(pady=20)

# Ẩn cửa sổ chính (chỉ hiển thị nút)
window.mainloop()
