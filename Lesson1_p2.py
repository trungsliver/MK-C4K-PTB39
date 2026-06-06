# Variables: Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thể thay đổi được khi lập trình

# Khai báo biến: [Tên biến] = [Giá trị]
    # Khai báo 1 biến
name = 'Duc Trung'
    # Khai báo nhiều biến
a, b, c = 1, 2, 3

# Quy tắc đặt tên biến:
    # Chỉ gồm chữ, số và dấu gạch dưới
    # Không bắt đầu bằng số
    # Không trùng với từ khóa của Python

# 2 Kiểu tên biến thường dùng:
    # camelCase (lạc đà): viết hoa chữ cái đầu của mỗi từ, trừ từ đầu tiên
myName = 'Duc Trung'
ageGreaterThan18 = True
    # snake_case (rắn): dùng dấu gạch dưới để phân tách các từ
my_name = 'Duc Trung'
age_greater_than_18 = True

# Data types: Kiểu dữ liệu
    # String: chuỗi / xâu ký tự
name = 'Duc Trung'
    # int (integer): số nguyên
age = 2
    # float: số thực (có phần thập phân)
score = 9.5
    # bool / boolean: logic, chỉ gầm True / False
isMale = True

# Kiểm tra kiểu dữ liệu: type()
print('Kiểu dữ kiệu của name:', type(name))
print('Kiểu dữ kiệu của age:', type(age))
print('Kiểu dữ kiệu của score:', type(score))
print('Kiểu dữ kiệu của isMale:', type(isMale))

# Chuyển đổi kiểu dữ liệu:
a = '123'
print('Kiểu dữ kiệu của a:', type(a))

b = int(a)
print('Kiểu dữ kiệu của b:', type(b))

# Nhập dữ liệu - input
# score = input('Nhập điểm: ')
# print('Kiểu dữ kiệu của score:', type(score))

# score2 = float(input('Nhập điểm: '))
# print('Kiểu dữ kiệu của score2:', type(score2))

# 4 cách hiển thị dữ liệu:
    # Cách 1: Dùng dấu +
print('Họ tên: ' + name)
print('Tuổi: ' + str(age))
    # Cách 2: Dùng dấu ,
print('Điểm số:', score)
print('Giới tính nam:', isMale)
    # Cách 3: Dùng f-string
print(f'Tên tôi là {name}. Tôi {age} tuổi.')
    # Cách 4: Hiển thị trên nhiều dòng
print(f'''
========== THÔNG TIN ==========
Họ tên: {name}
Tuổi: {age}
Điểm số: {score}
Giới tính nam: {isMale}
===============================
''')

# Toán tử số học:
    # Cơ bản: +, -, *, /
print('7 / 2 =', 7/2)        # 3.5
    # Chia lấy nguyên: //
print('7 // 2 =', 7//2)      # 3
    # Chia lấy dư: %
print('7 % 2 =', 7%2)        # 1
    # Lũy thừa: ** (thực hiện từ phải qua trái)
print('7 ** 2 =', 7**2)      # 49
print('2 ** 2 ** 3 =', 2 ** 2 ** 3)    

# =============== BÀI TẬP ===============
# Bài 1: Chuyển đổi USD sang VND
    # Nhập số USD muốn chuyển (float)
usd = float(input('Nhập số USD muốn chuyển: $'))
    # Đổi USD sang VND (1 USD = 27 000 VND)
vnd = usd * 27000
    # Hiển thị kết quả
print(f'{usd} USD = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng của HCN
# Tính diện tích và chu vi của HCN
    # Nhập chiều dài và chiều rộng (float)
length = float(input('Nhập chiều dài của HCN: '))
width = float(input('Nhập chiều rộng của HCN: '))
    # Tính diện tích và chu vi
area = length * width
perimeter = 2 * (length + width)
    # Hiển thị kết quả
print('Diện tích của HCN là:', area)
print('Chu vi của HCN là:', perimeter)
