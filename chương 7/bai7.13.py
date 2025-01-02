import tkinter as tk
from tkinter import messagebox

# Cấu trúc dữ liệu lưu trữ thông tin các bài tập
exercises = {
    '1.1': {'title': 'Lập trình hướng đối tượng', 'content': 'Giải phương trình bậc 2'},
    # ... các bài tập khác
}

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Hệ thống bài tập Python nâng cao")

# Tạo menu
menu = tk.Menu(window)
window.config(menu=menu)

# Tạo các menu con cho từng chương
for chapter in range(1, 8):
    chapter_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label=f"Chương {chapter}", menu=chapter_menu)

    for exercise in range(1, 10):
        exercise_name = f"{chapter}.{exercise}"
        if exercise_name in exercises:
            chapter_menu.add_command(label=exercise_name, command=lambda name=exercise_name: show_exercise_info(name))

# Hàm hiển thị thông tin bài tập
def show_exercise_info(exercise_name):
    exercise = exercises[exercise_name]
    messagebox.showinfo(title=exercise['title'], message=exercise['content'])

# Khởi chạy chương trình
window.mainloop()