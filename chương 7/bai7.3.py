import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Thay Đổi Kiểu Phông Chữ")

# Tạo nhãn (label) và thay đổi kiểu phông chữ
label = tk.Label(window, text="Chào mừng đến với Tkinter!", 
                 font=("Arial", 16, "bold"))  # Phông chữ Arial, cỡ 16, đậm
label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()