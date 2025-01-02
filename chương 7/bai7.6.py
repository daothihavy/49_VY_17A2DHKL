import tkinter as tk

def reverse_text_manually():
    input_text = entry.get()
    reversed_text = ""  # Chuỗi ngược sẽ được tạo thủ công
    for char in input_text:
        reversed_text = char + reversed_text
    result_label.config(text=reversed_text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Reverse Text")

# Nhãn và ô nhập liệu
entry_label = tk.Label(root, text="Enter a word:")
entry_label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

# Nút Validate
validate_button = tk.Button(root, text="Validate", command=reverse_text_manually)
validate_button.pack()

# Nhãn kết quả
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

# Chạy chương trình
root.mainloop()
