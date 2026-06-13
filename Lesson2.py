# Toán tử số học với string
    # Cộng chuỗi
print('Hello' + ' ' + 'Phúc')
    # Phép lặp (nhân)
print('hi' * 3)
print('hi' * 0)

# Toán tử số học (đã học buổi trước)

# Toán tử quan hệ (phép so sánh) => True/False
    # So sánh bằng: ==
print("7 == 2 :", 7 == 2)    # Kết quả: False
    # So sánh khác: !=
print("7 != 2 :", 7 != 2)    # Kết quả: True
    # So sánh lớn/nhỏ hơn: >, <, >=, <=
print("5 >= 5 :", 5 >= 5)           # Output: True
print("5 < 3 :", 5 < 3)            # Output: False

# Toán tử logic: and (&&), or (||), not (!)
    # Ví dụ: trà sữa - gà rán

#  Câu điều kiện (if-else statement)
    # Dạng 1: Dạng thiếu
age = 2
if age >= 18:
    print('Bạn đã đủ 18 tuổi')

    # Dạng 2: Dạng đủ
number = 11
if number % 2 == 0:
    print(number, 'là số chẵn')
else:
    print(number, 'là số lẻ')

    # Dạng 3: Dạng đa nhánh
# Xếp loại học lực: 
    # [8, 10]: Giỏi
    # [6.5, 8): Khá
    # [5, 6.5): Trung bình
    # [0, 5): Yếu
score = 8
if 8 <= score <= 10:
    print('Học lực: Giỏi')
elif 6.5 <= score < 8:
    print('Học lực: Khá')
elif 5 <= score < 6.5:
    print('Học lực: Trung bình')
elif 0 <= score < 5:
    print('Học lực: Yếu')
else:
    print('Điểm không hợp lệ')

# Switch-case
day = 3
match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _: # Default case
        print('Ngày không hợp lệ')

# ============== LUYỆN TẬP ==============
# Bài 1: Viết chương trình nhập vào một số nguyên n, 
# kiểm tra số đó có chia hết cho 5 hay không và in kết quả ra màn hình

# Bài 2: Nhập điểm số của bạn từ bàn phím.
# Yêu cầu: Xếp loại học lực học sinh. Biết rằng:
    # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu