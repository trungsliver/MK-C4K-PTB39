# Vòng lặp vô hạn - Vòng lặp while

# Ví dụ: Hiển thị các số nguyên từ 0 đến 5
    # Vòng lặp for:
for i in range(6): # range(0, 6, 1)
    print(i)

    # Vòng lặp while:
i = 0
while i <= 5:
    print(i)
    # tăng i lên 1 đơn vị
    i += 1      # i = i + 1

# Ví dụ: Nhập số nguyên n trong khoảng [0, 100]
# Nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input("Nhập số nguyên n trong khoảng [0, 100]: "))
# while n < 0 or n > 100:
#     print("Nhập sai! Vui lòng nhập lại.")
#     n = int(input("\nNhập số nguyên n trong khoảng [0, 100]: "))
# print('Nhập n thành công!')

# Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
    # Khi người chơi đoán đúng, hiển thị số lần người chơi đã đoán

import random
# Lấy ngẫu nhiên 1 số nguyên trong khoảng [0, 100]
number = random.randint(0, 100)

# Biến số đếm số lần đoán
count = 1

# guess = int(input("Nhập dự đoán: "))

# while guess != number:
#     if guess < number:
#         print("Số bạn đoán nhỏ hơn số đặc biệt.")
#     if guess > number:
#         print("Số bạn đoán lớn hơn số đặc biệt.")
#     # Tăng biến đếm lên 1
#     count += 1
#     guess = int(input("\nNhập dự đoán: "))
# print(f"Bạn đã đoán đúng sau {count} lần đoán.")

# ================== ÔN TẬP VÒNG LẶP FOR =====================
# Dạng 1: In / hiển thị ra màn hình
    # 1.1. In ra màn hình các số từ 0 đến n
n = 10
print(f'Các số trong khoảng [0, {n}]:')
for i in range(n+1):
    print(i, end = ' ')

    # 1.2. In ra màn hình các số nguyên trong khoảng [a, b]
a = 5
b = 10
print(f'\nCác số nguyên trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    print(i, end = ' ')

    # 1.3. In ra màn hình các số chẵn trong khoảng [a, b]
a, b = 10, 30
print(f'\nCác số chẵn trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end = ' ')

    # 1.4. In ra màn hình các số lẻ trong khoảng [a, b]
a, b = 10, 30
print(f'\nCác số lẻ trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    if i % 2 != 0:
        print(i, end = ' ')

# Dạng 2: Tính tổng
    # 2.1. Tính tổng các số trong khoảng [a, b]
a, b = 1, 5
total = 0       # Biến lưu tổng các số
for i in range(a, b+1):
    # Cộng dồn các số vào total
    total += i      # total = total + i
print(f'\nTổng các số trong khoảng [{a}, {b}] là: {total}')

total2 = [i for i in range(a, b+1)]

    # 2.2. Tính tổng các số chẵn trong khoảng [a, b]
a, b = 1, 5
total_even = 0       # Biến lưu tổng các số
for i in range(a, b+1):
    if i % 2 == 0:
        total_even += i      # total_even = total_even + i
print(f'\nTổng các số chẵn trong khoảng [{a}, {b}] là: {total_even}')

total_even2 = sum([i for i in range(a, b+1) if i % 2 == 0])
print(f'\nTổng các số chẵn trong khoảng [{a}, {b}] là: {total_even2}')


    # 2.3. Tính tổng các số lẻ trong khoảng [a, b]
a, b = 1, 5
total_odd = 0      
for i in range(a, b+1):
    if i % 2 != 0:
        total_odd += i      
print(f'\nTổng các số lẻ trong khoảng [{a}, {b}] là: {total_odd}')

total_odd2 = sum([i for i in range(a, b+1) if i % 2 != 0])
print(f'\nTổng các số lẻ trong khoảng [{a}, {b}] là: {total_odd2}')

# Dạng 3: Đếm số lượng
    # 3.1. Đếm số lượng các số chẵn trong khoảng [a, b]
a, b = 0, 10
count_even = 0
for i in range(a, b+1):
    if i % 2 == 0:
        count_even += 1
print(f'\nSố lượng các số chẵn trong khoảng [{a}, {b}] là: {count_even}')

count_even2 = sum([1 for i in range(a, b+1) if i % 2 == 0])
print(f'\nSố lượng các số chẵn trong khoảng [{a}, {b}] là: {count_even2}')

    # 3.2. Đếm số lượng số lẻ trong khoảng [a,b]
a, b = 0, 10
count_odd = 0
for i in range(a, b+1):
    if i % 2 != 0:
        count_odd += 1
print(f'\nSố lượng các số lẻ trong khoảng [{a}, {b}] là: {count_odd}')

count_odd2 = sum([1 for i in range(a, b+1) if i % 2 != 0])
print(f'\nSố lượng các số lẻ trong khoảng [{a}, {b}] là: {count_odd2}')
