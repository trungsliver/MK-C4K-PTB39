# Quy tắc đặt tên file: [Lớp]_[Hoten]_CP2.py
# Ví dụ: PTB39_DucTrung_CP2.py

# Link đề bài:: shorturl.at/azfDc

# Trắc nghiệm
# 1A 2B 3C 4D ...

# Tự luận
# ............

# Các câu lệnh điều khiển vòng lặp
    # break: thoát khỏi vòng lặp, bỏ qua các lần lặp còn lại
    # countinue: bỏ qua lần lặp hiện tại, tiếp tục vòng lặp
print('Ví dụ break:')
for i in range(10):
    if i == 5:
        break
    print(i, end = ' ')

print('Ví dụ continue:')
for i in range(10):
    if i == 5:
        continue
    print(i, end = ' ')

# Vấn đáp - Trắc nghiệm - Tự luận
# Châu Anh:     2/2     9/10    9/10    = 9
# Gia Linh:     2/2     8/10    9/10    = 8.5
# Nam Phong:    0.5/2   6/10    9/10    = 7
# Huy Quang:    2/2     9/10    9/10    = 9
# Khải Linh:    1.5/2   9/10    9/10    = 9
# Đức Huy:      1/2     8/10    9/10    = 8
# Bảo Phúc:     2/2     9/10    10/10   = 9.5

# ========================= LUYỆN TẬP =========================
a = [5, 2, 8, 1, 9, 3, 7, 4, 6]
# Bài 1: Viết chương trình nhập từ bàn phím danh sách a. Hãy trả về kết quả các phần tử trong danh sách theo thứ tự tăng dần.
a.sort()
print('Danh sách a theo thứ tự tăng dần:', a)

# Bài 2: Viết chương trình nhập từ bàn phím danh sách a. Hãy tìm ra phần tử lớn nhất và nhỏ nhất từ danh sách a và trả về kết quả.
print('Phần tử lớn nhất trong danh sách a:', max(a))
print('Phần tử nhỏ nhất trong danh sách a:', min(a))

# Bài 3: Viết chương trình nhập từ bàn phím danh sách a. Hãy tính giá trị trung bình của các phần tử trong danh sách a và trả về kết quả giá trị trung bình.
    # Tính tổng phần tửu danh sách
total = 0
for item in a:
    total += item

    # trung bình cộng = tổng / số phần tử
average = total / len(a)
print('Giá trị trung bình của các phần tử trong danh sách a:', average)

# Bài 4: Viết chương trình nhập từ bàn phím danh sách a. Tính tổng các số lẻ và tổng các số chẵn trong danh sách a.
total_even = 0
total_odd = 0
for item in a:
    if item % 2 == 0:
        total_even += item
    else:
        total_odd += item
print('Tổng các số chẵn trong danh sách a:', total_even)
print('Tổng các số lẻ trong danh sách a:', total_odd)

# Bài 5: Viết chương trình khai báo sẵn danh sách a. Viết chương trình bao gồm các chức năng: hiện toàn bộ phần tử danh sách, thêm phần tử vào danh sách, sửa phần tử danh sách, xóa phần tử trong danh sách.
while True:
    print('\nDanh sách a:', a)
    print('===== Chọn chức năng =====')
    print('1. Thêm phần tử vào danh sách')
    print('2. Sửa phần tử trong danh sách')
    print('3. Xóa phần tử trong danh sách')
    print('4. Thoát chương trình')
    print('===========================')
    choice = input('Nhập lựa chọn của bạn (1-4): ').strip()
    
    match choice:
        case '1':
            new_item = int(input('Nhập phần tử mới: '))
            a.append(new_item)
        case '2':
            index = int(input('Nhập vị trí phần tử cần sửa (0-{}): '.format(len(a)-1)))
            if 0 <= index < len(a):
                new_value = int(input('Nhập giá trị mới: '))
                a[index] = new_value
            else:
                print('Vị trí không hợp lệ.')
        case '3':
            index = int(input('Nhập vị trí phần tử cần xóa (0-{}): '.format(len(a)-1)))
            if 0 <= index < len(a):
                a.pop(index)
            else:
                print('Vị trí không hợp lệ.')
        case '4':
            break
        case _:
            print('Lựa chọn không hợp lệ. Vui lòng thử lại.')