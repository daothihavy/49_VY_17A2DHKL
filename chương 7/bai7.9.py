import tkinter as tk
from tkinter import ttk
from math import gcd

def calculate():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        operation = combo_function.get()
        
        if operation == "GCD":
            result = gcd(m, n)
            label_result.config(text=f"GCD({m}, {n}) = {result}")
        elif operation == "LCM":
            result = (m * n) // gcd(m, n)
            label_result.config(text=f"LCM({m}, {n}) = {result}")
        else:
            label_result.config(text="Please select a valid function.")
    except ValueError:
        label_result.config(text="Invalid input. Please enter integers.")

# Create the main window
root = tk.Tk()
root.title("GCD and LCM Calculator")

# Input fields
tk.Label(root, text="Enter value of m:").grid(row=0, column=0, padx=5, pady=5)
entry_m = tk.Entry(root)
entry_m.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Enter value of n:").grid(row=1, column=0, padx=5, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1, padx=5, pady=5)

# Function dropdown
tk.Label(root, text="Choose function:").grid(row=2, column=0, padx=5, pady=5)
combo_function = ttk.Combobox(root, values=["GCD", "LCM"])
combo_function.grid(row=2, column=1, padx=5, pady=5)

# Result label
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()