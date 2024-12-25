### Bài 6:
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def count(self):
        return len(self.items)

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents:", self.items)

# Ví dụ 
stack = Stack()
stack.push(50)
stack.push(20)
stack.push(90)
stack.print_stack() 
stack.pop()
stack.print_stack()



### Bài 7:
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
    
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        return 0
    
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")
    

    def next(self):
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1



### Bài 8:
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

class Employee:
    def __init__(self, name, birth_date, join_date):
        self.name = name  
        self.birth_date = birth_date 
        self.join_date = join_date  

    def display_info(self):
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.join_date.display()
        print("-" * 30)

employees = []  # Danh sách nhân viên
n = int(input("Nhập số lượng nhân viên: "))

for i in range(n):
    print(f"\nNhân viên {i + 1}:")
    name = input("Nhập họ tên: ")

    # Nhập ngày sinh
    day = int(input("Nhập ngày sinh: "))
    month = int(input("Nhập tháng sinh: "))
    year = int(input("Nhập năm sinh: "))
    birth_date = Date(day, month, year)

    # Nhập ngày vào công ty
    day = int(input("Nhập ngày vào công ty: "))
    month = int(input("Nhập tháng vào công ty: "))
    year = int(input("Nhập năm vào công ty: "))
    join_date = Date(day, month, year)

    # Tạo nhân viên và thêm vào danh sách
    employee = Employee(name, birth_date, join_date)
    employees.append(employee)

# Hiển thị thông tin nhân viên
print("\nThông tin nhân viên:")
for emp in employees:
    emp.display_info()


    ### Bài 9:
# Lớp Đa giác
class DaGiac:
    def __init__(self):
        self.sides = 0 

# Lớp Hình bình hành (HBH) kế thừa từ Đa giác
class HBH(DaGiac):
    def __init__(self, base, side, height):
        super().__init__()
        self.base = base  
        self.side = side 
        self.height = height 

# Lớp Hình chữ nhật (HCN) kế thừa từ Hình bình hành
class HCN(HBH):
    def __init__(self, length, width):
        super().__init__(length, width, width) 
        self.length = length  
        self.width = width  

# Lớp Hình vuông kế thừa từ Hình chữ nhật
class HinhVuong(HCN):
    def __init__(self, side):
        super().__init__(side, side)  
        self.side = side  

# Nhập số liệu cho Hình bình hành
base = float(input("Nhập cạnh đáy hình bình hành: "))
side = float(input("Nhập cạnh bên hình bình hành: "))
height = float(input("Nhập chiều cao hình bình hành: "))
hinh_binh_hanh = HBH(base, side, height)

# Tính chu vi và diện tích Hình bình hành
chu_vi_hbh = 2 * (hinh_binh_hanh.base + hinh_binh_hanh.side)
dien_tich_hbh = hinh_binh_hanh.base * hinh_binh_hanh.height
print(f"Chu vi hình bình hành: {chu_vi_hbh}")
print(f"Diện tích hình bình hành: {dien_tich_hbh}")
print("-" * 30)

# Nhập số liệu cho Hình chữ nhật
length = float(input("Nhập chiều dài hình chữ nhật: "))
width = float(input("Nhập chiều rộng hình chữ nhật: "))
hinh_chu_nhat = HCN(length, width)

# Tính chu vi và diện tích Hình chữ nhật
chu_vi_hcn = 2 * (hinh_chu_nhat.length + hinh_chu_nhat.width)
dien_tich_hcn = hinh_chu_nhat.length * hinh_chu_nhat.width
print(f"Chu vi hình chữ nhật: {chu_vi_hcn}")
print(f"Diện tích hình chữ nhật: {dien_tich_hcn}")
print("-" * 30)

# Nhập số liệu cho Hình vuông
side = float(input("Nhập cạnh của hình vuông: "))
hinh_vuong = HinhVuong(side)

# Tính chu vi và diện tích Hình vuông
chu_vi_hv = 4 * hinh_vuong.side
dien_tich_hv = hinh_vuong.side * hinh_vuong.side
print(f"Chu vi hình vuông: {chu_vi_hv}")
print(f"Diện tích hình vuông: {dien_tich_hv}")




### Bài 10:
import math

# Lớp Điểm
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x  
        self.y = y  

# Lớp Elip kế thừa từ lớp Điểm
class Elip(Diem):
    def __init__(self, x, y, ban_truc_lon, ban_truc_nho):
        super().__init__(x, y) 
        self.ban_truc_lon = ban_truc_lon  
        self.ban_truc_nho = ban_truc_nho  

    def tinh_dien_tich(self):
        return math.pi * self.ban_truc_lon * self.ban_truc_nho  

# Lớp Đường tròn kế thừa từ lớp Elip
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)
        self.ban_kinh = ban_kinh 

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2 

# Nhập số liệu cho Elip
x = float(input("Nhập tọa độ x của elip: "))
y = float(input("Nhập tọa độ y của elip: "))
ban_truc_lon = float(input("Nhập bán trục lớn của elip: "))
ban_truc_nho = float(input("Nhập bán trục nhỏ của elip: "))
elip = Elip(x, y, ban_truc_lon, ban_truc_nho)

# Tính diện tích của Elip
dien_tich_elip = elip.tinh_dien_tich()
print(f"Diện tích elip: {dien_tich_elip}")

# Nhập số liệu cho Đường tròn
ban_kinh = float(input("Nhập bán kính của đường tròn: "))
duong_tron = DuongTron(x, y, ban_kinh)

# Tính diện tích của Đường tròn
dien_tich_duong_tron = duong_tron.tinh_dien_tich()
print(f"Diện tích đường tròn: {dien_tich_duong_tron}")




### Bài 11:
import math

# Lớp Tam giác
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a 
        self.b = b  
        self.c = c  

    def tinh_dien_tich(self):
        p = (self.a + self.b + self.c) / 2 
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) 

# Lớp Tam giác vuông kế thừa từ lớp Tam giác
class TamGiacVuong(TamGiac):
    def __init__(self, canh_a, canh_b):
        # Hai cạnh góc vuông
        super().__init__(canh_a, canh_b, math.sqrt(canh_a**2 + canh_b**2))  

    def tinh_dien_tich(self):
        return 0.5 * self.a * self.b 

# Lớp Tam giác cân kế thừa từ lớp Tam giác
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        super().__init__(canh_bang, canh_bang, canh_khac)  

# Lớp Tam giác đều kế thừa từ lớp Tam giác cân
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)  

    def tinh_dien_tich(self):
        return (math.sqrt(3) / 4) * self.a**2  

# Nhập số liệu cho Tam giác vuông
canh_a = float(input("Nhập cạnh a của tam giác vuông: "))
canh_b = float(input("Nhập cạnh b của tam giác vuông: "))
tam_giac_vuong = TamGiacVuong(canh_a, canh_b)

# Tính diện tích Tam giác vuông
dien_tich_tgv = tam_giac_vuong.tinh_dien_tich()
print(f"Diện tích tam giác vuông: {dien_tich_tgv}")

# Nhập số liệu cho Tam giác đều
canh = float(input("Nhập cạnh của tam giác đều: "))
tam_giac_deu = TamGiacDeu(canh)

# Tính diện tích Tam giác đều
dien_tich_tgd = tam_giac_deu.tinh_dien_tich()
print(f"Diện tích tam giác đều: {dien_tich_tgd}")