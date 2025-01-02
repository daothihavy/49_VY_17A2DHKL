import tkinter as tk

# Tạo cửa sổ chính
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Cửa Sổ Tkinter")

# Tạo nhãn (label)
label = tk.Label(window, text="Chào mừng đến với Tkinter!")
label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()