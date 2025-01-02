import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Hàm chuyển đổi năm Dương lịch sang năm Âm lịch và con giáp
def convert_to_lunar():
    try:
        # Lấy năm Dương lịch từ ô TextBox
        year = int(entry_year.get())
        
        # Danh sách các con giáp theo chu kỳ 12 năm
        animals = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        
        # Tính con giáp và năm Âm lịch
        lunar_year = (year - 3) % 12  # Năm 2023 là năm Quý Mão (năm 2023 = năm Mão)
        animal = animals[lunar_year]
        
        # Hiển thị kết quả
        result_message = f"Năm Âm lịch là {animal} ({year})"
        
        # Tải và hiển thị hình ảnh con giáp tương ứng
        image_path = f"{animal}.png"  # Lưu các hình ảnh theo tên con giáp (Ví dụ: Tý.png, Sửu.png...)
        img = Image.open(image_path)
        img = img.resize((150, 150))  # Điều chỉnh kích thước ảnh
        img = ImageTk.PhotoImage(img)
        
        # Hiển thị thông báo và hình ảnh
        messagebox.showinfo("Kết quả", result_message)
        label_image.config(image=img)
        label_image.image = img  # Lưu ảnh vào thuộc tính của label để không bị xóa

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm Dương lịch hợp lệ!")

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chuyển Đổi Năm Dương Lịch sang Âm Lịch")

# Tạo nhãn, ô nhập năm Dương lịch và nút chuyển đổi
label_prompt = tk.Label(window, text="Nhập năm Dương lịch:")
label_prompt.pack(pady=10)

entry_year = tk.Entry(window)
entry_year.pack(pady=5)

convert_button = tk.Button(window, text="Chuyển đổi", command=convert_to_lunar)
convert_button.pack(pady=20)

# Tạo nhãn để hiển thị hình ảnh con giáp
label_image = tk.Label(window)
label_image.pack(pady=10)

# Chạy vòng lặp chính của cửa sổ
window.mainloop()