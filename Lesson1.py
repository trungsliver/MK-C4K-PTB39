# Ghi chú: ctrl /

# In / Hiển thị ra màn hình
print("Hello World")
print('Duc Trung')

# Biến số - Variables
    # Dùng để lưu trữ dữ liệu
    # Có thể thể thay đổi được khi lập trình
name = 'Duc Trung'
age = 2
a, b, c = 1, 2, 3

print(age)

# Nhập dữ liệu - Input
# game = input('Nhập game bạn thích: ')
# print(game)

# food = input('Nhập đồ ăn bạn thích: ')
# print(food)

# Các cách hiển thị dữ liệu (4 cách)
    # Cách 1: Dùng dấu +
print('Họ tên: ' + name)
    # Cách 2: Dùng dấu ,
print('Tuổi:', age)
    # Cách 3: Dùng f-string
print(f'Tên tôi là {name}. Tôi {age} tuổi')
    # Cách 4: Hiển thị trên nhiều dòng
print(f'''
========== THÔNG TIN ==========
Họ tên: {name}
Tuổi: {age}
Lớp: MK-C4K-PTB39
Trường học Công nghệ MindX
===============================
''')