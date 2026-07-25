# Danh sách: Array / List
# Thao tác cơ bản: CRUD (create, read, update, delete)

# Create - Khởi tạo danh sách
    # Danh sách rỗng (không có phần tử)
arr = []
    # Danh sách có sẵn phần tử
ptb39 = ['Quang', 'Huy', 'Phúc', 'C.Anh', 'G.Linh', 'K.Linh', 'Phong']
arr1 = ['age', 15, 1.2, True]

# Read - Duyệt, hiện phần tử
    # len() - độ dài / số lượng phần tử của danh sách
print('Số lượng phần tử của ptb39:', len(ptb39))
print('Số lượng phần tử của arr:', len(arr))

    # Hiện phần tử bằng chỉ số (index)
print('Phần tử đầu tiên:', ptb39[0])
print('Phần tử có index = 3:', ptb39[3])
print('Phần tử cuối cùng:', ptb39[6])
print('Phần tử cuối cùng:', ptb39[-1])

    # Duyệt danh sách
        # cách 1: Dùng cả index và value
for i in range(len(ptb39)):
    print(f'index = {i}, value = {ptb39[i]}')
        # cách 2: Dùng value
for item in ptb39:
    print('value =', item)
        # cách 3: Dùng enumerate() - hàm có sẵn Python
for index, value in enumerate(ptb39):
    print(f'index = {index}, value = {value}')

    # Hiển thị tất cả phần tử (dùng để test)
print('Danh sách ptb39:', ptb39)

# Update - Cập nhật phần tử
    # Thêm phần tử vào cuối danh sách - append(value)
ptb39.append('Trung')
    # Thêm vào vị trí chỉ định - insert(index, value)
ptb39.insert(2, 'imposter')
    # Chỉnh sửa phần tử có sẵn
ptb39[2] = 'Donald Trump'

# Delete - Xóa phần tử
    # Xóa bằng giá trị - remove(value)
ptb39.remove('Trung')
    # Xóa bằng chỉ số - pop(index)
ptb39.pop(2)
    # Xóa toàn bộ danh sách - clear()
ptb39.clear()

# Sắp xếp phần tử - sort()
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Theo thứ tự tăng dần
num_list.sort()
print('Danh sách tăng dần:', num_list)
    # Theo thứ tự giảm dần
num_list.sort(reverse=True)
print('Danh sách giảm dần:', num_list)

# Tìm giá trị phần tử lớn nhất / nhỏ nhất
print('Phần tử lớn nhất:', max(num_list))
print('Phần tử nhỏ nhất:', min(num_list))

# ============ LUYỆN TẬP ===============
# Bài 1: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó

n = int(input('Nhập số nguyên n: '))    
    # Khai báo biến count để đếm số lượng ước số của n
count = 0

    # Duyệt i trong khoảng từ 1 đến n
for i in range(1, n + 1):
    # Nếu n chia hết cho i thì tăng biến count lên 1
    if n % i == 0:
        count += 1

    # Hiển thị kết quả
if count == 2:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [50,100] và tính tổng các số đó
    # Khai báo biến lưu tổng các snt
total = 0
    # Duyệt n trong khoảng [50,100]
for n in range(50, 101):
    # Biến đếm số ước của n
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    # Nếu n là số nguyên tố
    if count == 2:
        # Hiển thị n
        print(n, end=' ')
        # Cộng n vào tổng
        total += n

print(f'\nTổng các số nguyên tố trong khoảng [50,100] là: {total}')