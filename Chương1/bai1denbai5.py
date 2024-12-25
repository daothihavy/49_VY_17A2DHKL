### BÀI 1
class HCN:
    def __init__(self):
        self.dai = 0
        self.rong = 0

    def nhap_du_lieu(self):
        self.dai = float(input("Nhập chiều dài: "))
        self.rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thong_tin(self):
        print(f"Chiều dài: {self.dai}")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

hinh_chu_nhat = HCN()
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.in_thong_tin()


### BÀI 3
class PS:
    def __init__(self):
        self.tu_so = 0
        self.mau_so = 1

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số (khác 0): "))
        while self.mau_so == 0:
            print("Mẫu số phải khác 0, vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def in_phan_so(self):
        if self.mau_so == 1:
            print(f"Phân số là: {self.tu_so}")
        else:
            print(f"Phân số là: {self.tu_so}/{self.mau_so}")

ps = PS()
ps.nhap_phan_so()

if ps.kiem_tra_hop_le():
    ps.in_phan_so()
else:
    print("Phân số không hợp lệ!")





### Bài 4:
class Stack:
    def __init__(self, capacity):

        self.capacity = capacity
        self.stack = []  
        self.top = -1    


    def isEmpty(self):
        return self.top == -1


    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.stack.append(value)
            self.top += 1
            print(f"Đã đưa {value} vào ngăn xếp.")

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng! Không thể lấy phần tử.")
            return None
        else:
            value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {value} từ ngăn xếp.")

    def __del__(self):
        print("Ngăn xếp đã bị hủy.")

capacity = int(input("Nhập dung lượng tối đa của ngăn xếp: "))
stack = Stack(capacity)

stack.push(4.6)
stack.push(9.9)
stack.push(9.8)

stack.pop()
stack.pop()

print("Ngăn xếp rỗng:", stack.isEmpty())
print("Ngăn xếp đầy:", stack.isFull())




### Bài 5:
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

# Ví dụ 
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.count())  
stack.pop()
print(stack.count())