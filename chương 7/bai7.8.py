import tkinter as tk

def find_divisors():
    try:
        # Lấy giá trị từ người dùng
        n = int(entry.get())
        divisors = [i for i in range(1, abs(n) + 1) if n % i == 0]
        
        # Hiển thị danh sách các ước
        result_label.config(
            text=f"The divisors of {n} are: {', '.join(map(str, divisors))}", 
            fg="blue"
        )
    except ValueError:
        # Xử lý nếu nhập không phải số nguyên
        result_label.config(text="Please enter a valid integer", fg="red")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Find Divisors")

# Tạo nhãn và ô nhập liệu
entry_label = tk.Label(root, text="Enter an integer N:")
entry_label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

# Nút thực thi
validate_button = tk.Button(root, text="Find Divisors", command=find_divisors)
validate_button.pack()

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="", fg="blue", wraplength=300, justify="left")
result_label.pack()

# Chạy vòng lặp chính của chương trình
root.mainloop()