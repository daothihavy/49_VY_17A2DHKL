import io
import requests
from tkinter import Tk, Label, Button, Entry
from PIL import Image, ImageTk

def hien_thi_anh(file_path):
    """Hiển thị ảnh từ file."""
    try:
        img = Image.open(file_path)
        tk_img = ImageTk.PhotoImage(img)
        label.config(image=tk_img)
        label.image = tk_img
    except Exception as e:
        label.config(text=f"Lỗi: {e}")

def hien_thi_anh_tu_url(url):
    """Hiển thị ảnh từ URL."""
    try:
        # Gửi yêu cầu tải ảnh từ URL
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi tải ảnh
        img_data = io.BytesIO(response.content)  # Lưu vào bộ nhớ tạm
        img = Image.open(img_data)
        tk_img = ImageTk.PhotoImage(img)
        label.config(image=tk_img)
        label.image = tk_img
    except Exception as e:
        label.config(text=f"Lỗi: {e}")

# Tạo giao diện Tkinter
root = Tk()
root.title("Hiển thị ảnh từ file hoặc URL")

# Nhập đường dẫn ảnh từ file hoặc URL
entry = Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Nút hiển thị ảnh từ file
btn_file = Button(root, text="Hiển thị từ file", command=lambda: hien_thi_anh(entry.get()))
btn_file.pack(padx=10, pady=5)

# Nút hiển thị ảnh từ URL
btn_url = Button(root, text="Hiển thị từ URL", command=lambda: hien_thi_anh_tu_url(entry.get()))
btn_url.pack(padx=10, pady=5)

# Thêm label để hiển thị ảnh
label = Label(root, text="Chưa có ảnh để hiển thị.")
label.pack(padx=10, pady=10)

# Vòng lặp chính
root.mainloop()

