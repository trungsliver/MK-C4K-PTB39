# Link đề bài: shorturl.at/EHuSe
# Bài 1:
a, b = 10, 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a ** b =", a ** b)
if b == 0:
    print("Không thể chia cho 0")
else:
    print("a / b =", a / b)
    print("a // b =", a // b)
    print("a % b =", a % b)


# Bài 2:
try:
    age1 = int(input("Nhập tuổi người thứ nhất: "))
    age2 = int(input("Nhập tuổi người thứ hai: "))
    age3 = int(input("Nhập tuổi người thứ ba: "))

    if age1 < 0 or age2 < 0 or age3 < 0:
        print("Tuổi không hợp lệ")
    else:
        if age1 <= age2 and age1 <= age3:
            print("Người thứ nhất là người nhỏ tuổi nhất")
        elif age2 <= age1 and age2 <= age3:
            print("Người thứ hai là người nhỏ tuổi nhất")
        elif age3 <= age1 and age3 <= age2:
            print("Người thứ ba là người nhỏ tuổi nhất")
        else:
            print("Có nhiều người cùng tuổi nhỏ nhất")
except:
    print("Nhập tuổi không hợp lệ")

# Bài 3:
n = int(input('Nhập số nguyên dương n: '))

if  n <= 0:
    print('Số nhập vào không hợp lệ')
else:
    print(f'Các số lẻ từ 1 đến {n} là:')
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end = ' ')

# Bài 4:  
n = int(input('Nhập số nguyên n: '))
if n < 0:
    print(f'Giá trị tuyệt đối của {n} là: {-n}')
else:
    print(f'Giá trị tuyệt đối của {n} là: {n}')

# Bài 5:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Số nhỏ nhất & số lớn nhất:
print(f'Số nhỏ nhất trong danh sách là: {min(numbers)}')
print(f'Số lớn nhất trong danh sách là: {max(numbers)}')
    # Tổng giá trị số lẻ
total_odd = 0
for num in numbers:
    if num % 2 != 0:
        total_odd += num
print(f'Tổng các số lẻ trong danh sách là: {total_odd}')

# Bài 6:
height_input = input("Nhập danh sách chiều cao (cách nhau bởi dấu cách hoặc dấu phẩy): ")
    # Thay toàn bộ dấu phẩy thành dấu cách
height_input = height_input.replace(',', ' ')
    # Tách chuỗi thành danh sách các chiều cao
        # strip(): loại bỏ khaorng trắng ở đầu và cuối chuỗi
        # split(): tách chuỗi thành danh sách các phần tử dựa trên khoảng trắng
height_list = height_input.strip().split()
print("Danh sách chiều cao đã nhập:", height_list)
    # Tìm người nhỏ hơn 1.5m
try:
    count = 0
    for height in height_list:
        if float(height) < 1.5:
            count += 1
    if count == 0:
        print("Không có người nào nhỏ hơn 1.5m")
    else:
        print(f"Số người có chiều cao nhỏ hơn 1.5m là: {count}")
except:
    print("Dữ liệu lỗi")

# Bài 7:
def calculate_average_score(scores):
    # Điểm cuối cùng được tính hệ số 2 => thểm điểm cuối cùng vào danh sách 1 lần nữa
    last_score = scores[-1]
    scores.append(last_score)
    # Tính tổng điểm
    total = 0
    for score in scores:
        total += score
    # Tính điểm trung bình
    average = total / len(scores)
    # Trả về điểm trung bình (làm tròn đến 2 chữ số thập phân)
    return round(average, 2)
arr = [7, 7, 8, 9] 
arr1 = [7, 8, 9, 8, 10, 5, 9]
print('Test arr:', calculate_average_score(arr))
print('Test arr1:', calculate_average_score(arr1))