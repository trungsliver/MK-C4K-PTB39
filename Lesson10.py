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

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
