import tkinter as tk

def calculate_sum():
    try:
        # Lấy giá trị N từ người dùng
        n = int(entry.get())
        if n < 1:
            result_label.config(text="Please enter a positive integer", fg="red")
            return
        
        # Tính tổng và biểu thức
        total_sum = 0
        expression = ""
        for i in range(1, n + 1):
            total_sum += i
            expression += f"{i} + " if i < n else f"{i} = {total_sum}"
        
        # Hiển thị kết quả
        result_label.config(text=f"The sum is {expression}", fg="blue")
    except ValueError:
        result_label.config(text="Please enter a valid integer", fg="red")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Sum Calculator")

# Nhãn và ô nhập liệu
entry_label = tk.Label(root, text="Enter value of integer N:")
entry_label.pack()

entry = tk.Entry(root, width=10)
entry.pack()

# Nút Validate
validate_button = tk.Button(root, text="Validate", command=calculate_sum)
validate_button.pack()

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

# Chạy chương trình
root.mainloop()

