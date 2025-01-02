import tkinter as tk

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            conclusion = "Underweight"
        elif 18.5 <= bmi < 24.9:
            conclusion = "Normal weight"
        elif 25 <= bmi < 29.9:
            conclusion = "Overweight"
        else:
            conclusion = "Obesity"

        label_bmi_result.config(text=f"BMI: {bmi}")
        label_conclusion.config(text=f"Conclusion: {conclusion}")
    except ValueError:
        label_bmi_result.config(text="Invalid input")
        label_conclusion.config(text="")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("BMI Calculator")

# Nhập cân nặng
tk.Label(root, text="Cân nặng (kg):").grid(row=0, column=0, padx=5, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

# Nhập chiều cao
tk.Label(root, text="Chiều cao (m):").grid(row=1, column=0, padx=5, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=5, pady=5)

# Nút tính BMI
button_calculate = tk.Button(root, text="Tính BMI", command=calculate_bmi)
button_calculate.grid(row=2, column=0, columnspan=2, pady=10)

# Hiển thị kết quả BMI
label_bmi_result = tk.Label(root, text="")
label_bmi_result.grid(row=3, column=0, columnspan=2, pady=5)

# Hiển thị kết luận
label_conclusion = tk.Label(root, text="")
label_conclusion.grid(row=4, column=0, columnspan=2, pady=5)

# Chạy vòng lặp chính
root.mainloop()
