import tkinter as tk
from tkinter import ttk, messagebox

def tinh_cuoc():
    try:
        # Lấy giá trị từ các trường nhập
        loai_xe = combo_loai_xe.get()
        so_km = float(entry_so_km.get())
        thoi_gian_cho = int(entry_thoi_gian_cho.get())
        
        if so_km < 0 or thoi_gian_cho < 0:
            raise ValueError
        
        # Giá mở cửa
        gia_mo_cua = 12000  # VND cho cả hai loại xe
        
        # Tính phí km
        if loai_xe == "Xe 4 chỗ":
            gia_km_30 = 15300
            gia_km_tren_30 = 12100
        elif loai_xe == "Xe 7 chỗ":
            gia_km_30 = 16100
            gia_km_tren_30 = 13800
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn loại xe.")
            return
        
        # Tính số km vượt mức
        if so_km <= 0.8:
            phi_km = gia_mo_cua
        else:
            so_km_tinh_phi = so_km - 0.8
            if so_km_tinh_phi <= 30:
                phi_km = gia_mo_cua + so_km_tinh_phi * gia_km_30
            else:
                phi_km = gia_mo_cua + 30 * gia_km_30 + (so_km_tinh_phi - 30) * gia_km_tren_30
        
        # Tính phí chờ
        if thoi_gian_cho <= 5:
            phi_cho = 0
        else:
            phi_cho = (thoi_gian_cho - 5) * 750
        
        # Tổng cước
        tong_cuoc = phi_km + phi_cho
        
        # Hiển thị kết quả
        label_ket_qua.config(text=f"Tổng cước: {tong_cuoc:,.0f} VND")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số liệu hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tính Cước Taxi")

# Loại xe
tk.Label(root, text="Loại xe:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
combo_loai_xe = ttk.Combobox(root, values=["Xe 4 chỗ", "Xe 7 chỗ"], state="readonly")
combo_loai_xe.grid(row=0, column=1, padx=10, pady=10)
combo_loai_xe.current(0)  # Chọn mặc định "Xe 4 chỗ"

# Số km đã đi
tk.Label(root, text="Số km đã đi:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_so_km = tk.Entry(root)
entry_so_km.grid(row=1, column=1, padx=10, pady=10)

# Thời gian chờ (phút)
tk.Label(root, text="Thời gian chờ (phút):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_thoi_gian_cho = tk.Entry(root)
entry_thoi_gian_cho.grid(row=2, column=1, padx=10, pady=10)

# Nút tính cước
button_tinh = tk.Button(root, text="Tính cước", command=tinh_cuoc)
button_tinh.grid(row=3, column=0, columnspan=2, pady=20)

# Hiển thị kết quả
label_ket_qua = tk.Label(root, text="Tổng cước: ", font=("Arial", 12, "bold"))
label_ket_qua.grid(row=4, column=0, columnspan=2, pady=10)

# Chạy vòng lặp chính
root.mainloop()
