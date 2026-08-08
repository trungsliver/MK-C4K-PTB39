# Hàm - Chương trình con
    # Khái niệm: 1 nhóm các câu lệnh thực hiện 1 nhiệm vụ cụ thể
    # Đặc điểm: có thể tái sử dụng (sử dụng lại nhiều lần)

# Cấu trúc cơ bản
def introduce():
    print('Tôi tên là Bảo Phúc')
    print('Tôi 12 tuổi')
    print('Tôi sống ở Hưng Yên')

    # Sử dụng hàm
introduce()

# Hàm có tham số đầu vào (parameter)
def introduce2(name:str, age:int, address):
    print('Tôi tên là', name)
    print('Tôi', age, 'tuổi')
    print('Tôi sống ở', address)

introduce2('Đức Huy', 12, 'Hà Nội')
introduce2('Khải Linh', 12, 'Hà Nội')

# return: trả về giá trị khi sử dụng hàm
    # Lưu ý: 
        # - Hàm có return sẽ sử dụng như 1 biến
        # - Khi gặp return, hàm sẽ dừng lại (giống câu lệnh break trong vòng lặp)

def area_rectangle(length, width):
    return length * width

    # Không hiển thị ra màn hình 
area_rectangle(5, 10) 
    # Hiển thị ra màn hình
print('Diện tích HCN:', area_rectangle(5, 10))

# ================ VÍ DỤ ================
    # Kiểm tra số chẵn - số lẻ
def check_even(number):
    if number % 2 == 0:
        print(number, 'là số chẵn')
    else:
        print(number, 'là số lẻ')
check_even(5)
check_even(6)

def check_even2(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(check_even2(5))
print(check_even2(6))

# ================== LUYỆN TẬP =======================
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers):
    total = 0                   # Khai báo biến lưu tổng
    for item in numbers:        # Duyệt danh sách, cách 2 - chỉ có giá trị
        if item % 2 != 0:       # Kiểm tra số lẻ
            total += item       # Cộng giá trị phần tử vào biến total
    return total                # Trả về giá trị total khi duyệt xong vòng lặp

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Tổng các số lẻ trong danh sách là:', sum_odd(arr))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n:int):
    count = 0                   # Khai báo biến đếm 
    for i in range(1, n + 1):   # Duyệt số từ 1 đến n
        if n % i == 0:          # Kiểm tra n có chia hết cho i không
            count += 1          # Chia hết thì tăng count thêm 1
    if count == 2:              # count = 2 thì n là số nguyên tố
        return True             # Trả về True
    else:                       # count != 2 thì n không phải số nguyên tố
        return False            # Trả về False

print('7:', is_prime(7))  # True
print('8:',is_prime(8))  # False

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s:str):
    # strip(): xóa khoảng trắng ở đầu và cuối chuỗi
    # split(): tách chuỗi và lưu các phần tử đc tách vào danh sách
    arr = s.strip().split()     # Chuyển chuỗi thành danh sách từ
    return len(arr)             # Kích thước danh sách = số lượng từ

str1 = '  Khải    Linh       mặc     áo     đỏ    '
print('Số lượng từ trong chuỗi:', count_words(str1))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n:int):
    total = 0
    while n > 0:                    # Duyệt số n cho đến khi n = 0
        total = total + n%10        # Lấy hàng đơn vị của n
        n = n // 10                 # Loại bỏ hàng đơn vị của n
    return total

print('Tổng các chữ số của 12345:', sum_of_digits(12345))

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
def find_max(arr):
    max_value = max(arr)        # Tìm giá trị lớn nhất của danh sách
    for i in range(len(arr)):   # Duyệt danh sách, cách 1 - có index, value
        if arr[i] == max_value: # Tìm vị trí của max_value
            return i            # Trả về vị trí
        
numbers = [10, 5, 1, 2, 6, 9999, 4, 9, 3, 7, 8]
print('Vị trí phần tử lớn nhất:', find_max(numbers))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n:int):
    sum = 0
    for i in range(1, n+1):  # Duyệt số từ 1 đến n
        sum = sum + i        # Tính tổng các số từ 1 đến n
    return sum
print('Tổng các số từ 1 đến 10:', sum_to_n(10))
