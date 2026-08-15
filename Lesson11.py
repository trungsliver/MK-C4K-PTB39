# ========================== Ôn tập ==========================
# Bài 1: Nhập vào từ bàn phím các thông tin các nhân: 
    # Họ tên, Tuổi, Trường học, giới tính, điểm trung bình.
    # In ra màn hình các thông tin vừa nhập
name = input('Nhập tên: ')
age = int(input('Nhập tuổi: '))
school = input('Nhập trường học: ')
gender = input('Nhập giới tính: ')
score = float(input('Nhập điểm trung bình: '))
print(f'''
Họ tên: {name}
Tuổi: {age}
Trường học: {school}
Giới tính: {gender}
Điểm: {score}''')

# Bài 2: Nhập vào chiều dài và chiều rộng hình chữ nhật
    # In ra màn hình chu vi và diện tích hình chữ nhật đó.
a = float(input('Nhập chiều dài: '))
b = float(input('Nhập chiều rộng: '))
chuvi = 2 * (a + b)
dtich = a * b
print(f'Chu vi HCN:', chuvi)
print(f'Diện tích HCN:', dtich)

# Bài 3: Nhập số nguyên n từ bàn phím.
    # Kiểm tra xem n có phải là số chẵn hay không.
n = int(input('Nhập số nguyên n: '))
if n % 2 == 0:
    print(f'{n} là số chẵn')
else:
    print(f'{n} là số lẻ')

# Bài 4: Nhập điểm số từ bàn phím. Hãy in ra mà hình xếp hạng học lực, biết rằng:
    # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
score = float(input('Hãy nhập điểm của bạn: '))
if 8 <= score <= 10:
    print('Xếp loại: Giỏi')
elif 6.5 <= score < 8:
    print('Xếp loại: Khá')
elif 5 <= score < 6.5:
    print('Xếp loại: Trung bình')
elif 0 <= score < 5:
    print('Xếp loại: Yếu')
else:
    print('Điểm không hợp lệ')

# Bài 5: Nhập 2 số nguyên a và b từ bàn phím
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
    # Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
if b >= a:
    print(f'Các số trong khoảng [{a}, {b}] là:')
    for i in range(a, b + 1):
        print(i, end = ' ')
else:
    print(f'Các số trong khoảng [{b}, {a}] là:')
    for i in range(b, a + 1):
        print(i, end = ' ')

    # Yêu cầu 2: Tính tổng các số chia hết cho 3 trog khoảng vừa in
sum = 0
if b >= a:
    for i in range(a, b + 1):       # Duyệt vòng lặp chạy từ a đến b
        if i % 3 == 0:              # Kiểm tra i chia hết cho 3
            sum += i                # Cộng i vào biến sum
    print(f'Tổng các số chia hết cho 3 trong khoảng [{a}, {b}] là:', sum)
else:
    for i in range(b, a + 1):       # Duyệt vòng lặp chạy từ b đến a
        if i % 3 == 0:              # Kiểm tra i chia hết cho 3
            sum += i                # Cộng i vào biến sum
    print(f'Tổng các số chia hết cho 3 trong khoảng [{b}, {a}] là:', sum)


    # Yêu cầu 3: In ra số lượng số lẻ có trong khoảng trên
count = 0
if b >= a:
    for i in range(a, b + 1):       # Duyệt vòng lặp chạy từ a đến b
        if i % 2 != 0:              # Kiểm tra số lẻ
            count += 1              # Tăng count thêm 1
    print(f'Số lượng số lẻ trong khoảng [{a}, {b}] là:', count)
else:
    for i in range(b, a + 1):       # Duyệt vòng lặp chạy từ b đến a
        if i % 2 != 0:              # Kiểm tra số lẻ
            count += 1              # Tăng count thêm 1
    print(f'Số lượng số lẻ trong khoảng [{b}, {a}] là:', count)

    # Yeu cầu 4: Tính trung bình cộng các số trong khoảng trên (làm tròn đến chữ số thập phân thứ 2)
sum = 0
count = 0
if b >= a:
    for i in range(a, b + 1):
        sum += i
        count += 1
    tbc = round(sum/count, 2)
    print(f'TBC các số trong khoảng [{a}, {b}] là:', tbc)
else:
    for i in range(b, a + 1):
        sum += i
        count += 1
    tbc = round(sum/count, 2)
    print(f'TBC các số trong khoảng [{a}, {b}] là:', tbc)

# Bài 6: In ra bảng cửu chương từ 5 đến 9
for i in range(5, 10):
    print('\nBảng cửu chương', i)
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')

# Bài 7: Nhập số nguyên dương n. Tính tổng tất cả các chữ số của n.
    # Ví dụ: n = 123 => Tổng các chữ số = 1+2+3 = 6
n = int(input('Nhập số nguyên dương n: '))   
sum = 0
while n > 0:              # Duyệt số n cho đến khi n = 0
    sum = sum + n%10      # Lấy hàng đơn vị của n
    n = n // 10           # Loại bỏ hàng đơn vị của n
print('Tổng các chữ số:', sum)

# Bài 8: Nhập n là số giây cần chuyển đổi (số nguyên)
    # In ra màn hình dạng h-m-s
    # Ví dụ: 3661s = 1h 1p 1s
    # Nhập số giây từ bàn phím
seconds = int(input("Nhập số giây cần chuyển đổi: "))
# Chuyển đổi số giây sang giờ, phút, giây
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

# Bài 9: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
a = input('Nhập danh sách: ')       # Mỗi phần tử cách nhau 1 khoảng trắng
arr1 = a.split()                    # split(): hàm tách chuỗi học ở lesson 11
        # Chuyển các phần tử từ kiểu str sang int
arr = []
for item in arr1:
    arr.append(int(item))
print(arr) 

    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
arr.insert(2,-5)

    # YC3: Tính tổng các số chẵn trong danh sách
sum_even = 0
for item in arr:                # Cách duyệt số 2: chỉ dùng value
    if item % 2 == 0:           # Kiểm tra số chẵn
        sum_even += item        # cộng phần tử chẵn vào biến tổng
print('Tổng các số chẵn:', sum_even)

    # YC4: Đếm số lượng số lẻ có trong danh sách
count_odd = 0
for item in arr:                # Cách duyệt số 2: chỉ dùng value
    if item % 2 != 0:           # Kiểm tra số lẻ
        count_odd += 1          # tăng count thêm 1
print('Số lượng số lẻ:', count_odd)

    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
print('Giá trị phần tử lớn nhất:', max(arr))

    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
index_min = 0
for i in range(len(arr)):       # Cách duyệt số 1: cả index và value
    if arr[i] == min(arr):      # tìm phần tử = giá trị phần tử nhỏ nhất
        index_min = i           # lưu index của phần tử đó vào biến
print('Vị trí số nhỏ nhất:', index_min)

    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách
def arr_avg(arr):
    sum = 0
    for item in arr:            # Cách duyệt số 2: chỉ dùng value
        sum += item             # cộng phần tử vào biến tổng
    avg = sum/len(arr)          # trung bình = tổng / số lượng phần tử
    return round(avg, 2)        # làm tròn đến chữ số thập phân số 2
print('Giá trị trung bình các phần tử:', arr_avg(arr))

# Bài 10: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
input_string = input("Nhập chuỗi các số nguyên (cách nhau bằng khoảng trắng hoặc dấu phẩy): ")
    # Yêu cầu 1: Tách chuỗi và thêm vào danh sách có tên num_list
input_string = input_string.replace(",", " ")   # Thay dấu phẩy thành dấu cách
num_list = input_string.split()                 # Tách chuỗi thành các phần tử trong danh sách

    # Yêu cầu 2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
num_list = [int(num) for num in num_list]

    # Yêu cầu 3: In ra màn hình số lượng số lẻ của num_list.
odd_count = 0               # Khởi tạo biến đếm số lẻ
for num in num_list:        # Duyệt từng phần tử trong danh sách
    if num % 2 != 0:        # Kiểm tra số lẻ
        odd_count += 1      # Tăng biến đếm
print(f"Số lượng số lẻ trong danh sách là: {odd_count}")
    # Yêu cầu 4: Sắp xếp các phần tử trong danh sách num_list theo thứ tự từ lớn đến nhỏ.
num_list.sort(reverse=True)  # Sắp xếp danh sách theo thứ tự giảm dần
print(f"Danh sách sau khi sắp xếp từ lớn đến nhỏ: {num_list}")

# Bài 11: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2.
import random
        # Tạo 2 danh sách arr1 và arr2 với các số ngẫu nhiên trong khoảng [20, 50]
arr1 = [random.randint(20, 50) for i in range(10)]  # Tạo 10 phần tử cho arr1
arr2 = [random.randint(20, 50) for i in range(10)]  # Tạo 10 phần tử cho arr2
        # In ra 2 danh sách tạo ra
print("Danh sách arr1:", arr1)
print("Danh sách arr2:", arr2)

    # Yêu cầu 1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo.
def phan_tu_chung(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                arr3.append(arr1[i])
    print(arr3)
phan_tu_chung(arr1, arr2)

    # Yêu cầu 2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
index_min = 0
for i in range(len(arr1)):          # Cách duyệt số 1: cả index và value
    if arr1[i] == min(arr1):        # tìm phần tử = giá trị phần tử nhỏ nhất
        index_min = i               # lưu index của phần tử đó vào biến
print('Vị trí số nhỏ nhất arr1:', index_min)

    # Yêu cầu 3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2
index_max = 0
for i in range(len(arr2)):          # Cách duyệt số 1: cả index và value
    if arr2[i] == min(arr2):        # tìm phần tử = giá trị phần tử nhỏ nhất
        index_max = i               # lưu index của phần tử đó vào biến
print('Vị trí số lớn nhất arr2:', index_max)

# Bài 12: Hãy nhập từ bàn phím họ tên của bạn.
full_name = input("Nhập họ tên của bạn: ")
    # Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa
uppercase_name = full_name.upper()
print("Tên viết hoa toàn bộ:", uppercase_name)

    # Yêu cầu 2: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết thường
lowercase_name = full_name.lower()
print("Tên viết thường toàn bộ:", lowercase_name)

    # Yêu cầu 3: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa các chữ cái đầu
title_case_name = full_name.title()
print("Tên viết hoa các chữ cái đầu:", title_case_name)
