import tkinter as tk

# Hàm xử lý khi nhấn nút "Gửi"
def send_data():
    name = entry_name.get()
    student_id = entry_id.get()
    password = entry_password.get()
    
    # In ra thông tin nhập vào (có thể thay đổi để gửi đến máy chủ hoặc lưu vào file)
    print("Tên sinh viên:", name)
    print("ID sinh viên:", student_id)
    print("Mật khẩu:", password)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Đăng Ký Sinh Viên")

# Tạo nhãn và hộp văn bản cho tên sinh viên
label_name = tk.Label(window, text="Tên sinh viên:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

# Tạo nhãn và hộp văn bản cho ID sinh viên
label_id = tk.Label(window, text="ID sinh viên:")
label_id.pack()
entry_id = tk.Entry(window)
entry_id.pack()

# Tạo nhãn và hộp văn bản cho mật khẩu
label_password = tk.Label(window, text="Mật khẩu:")
label_password.pack()
entry_password = tk.Entry(window, show="*")  # Ẩn mật khẩu khi nhập
entry_password.pack()

# Tạo nút "Gửi", nhưng ẩn nó ban đầu
button_send = tk.Button(window, text="Gửi", command=send_data)
button_send.pack()
button_send.pack_forget()  # Ẩn nút "Gửi" ban đầu

# Hàm kiểm tra thông tin và hiển thị nút "Gửi"
def check_and_show_button():
    if entry_name.get() and entry_id.get() and entry_password.get():  # Kiểm tra nếu các ô đều có giá trị
        button_send.pack()  # Hiển thị nút "Gửi"

# Cập nhật khi người dùng nhập thông tin
entry_name.bind("<KeyRelease>", lambda event: check_and_show_button())
entry_id.bind("<KeyRelease>", lambda event: check_and_show_button())
entry_password.bind("<KeyRelease>", lambda event: check_and_show_button())

# Chạy vòng lặp chính của cửa sổ
window.mainloop()