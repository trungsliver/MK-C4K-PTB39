# ========== CÁC HÀM THƯỜNG DÙNG VỚI STRING ==========

# String: chuỗi / xâu ký tự
class_name = 'Python App Basic 39'

# Độ dài string (số ký tự) - len()
print('Độ dài chuỗi class_name =', len(class_name))

# Truy cập từng ký tự trong string
    # Truy cập theo index
print('Ký tự đầu tiên =', class_name[0])
print('Ký tự cuối cùng =', class_name[-1])
print('Ký tự cuối cùng =', class_name[len(class_name)-1])

    # Duyệt string
        # Cách 1: Dùng cả index và value
for i in range(len(class_name)):
    print(f'index = {i}, value = {class_name[i]}')
        # Cách 2: Dùng value
for char in class_name:
    print('value =', char)

# Xâu con (substring)
str1 = 'Dang Chau Anh'
str2 = 'Chau Anh'
str3 = 'dep trai'

    # Kiểm tra substring: in
print('str2 in str1:', str2 in str1)    # True
print('str3 in str1:', str3 in str1)    # False

    # Tìm vị trí substring: find()
print('Vị trí str2 trong str1 =', str1.find(str2))      # 5
print('Vị trí str3 trong str1 =', str1.find(str3))      # -1 (không tìm thấy)

# Cắt chuỗi - slicing()
name = 'hahahihihuhu'
    # Cắt ở vị trí bất kì [start:end]
print('name[4,8] =', name[4:8])      # hihi
    # Cắt từ đầu đến vị trí bất kì [:end]
print('name[:4] =', name[:4])        # haha
    # Cắt từ vị trí bất kì đến cuối [start:]
print('name[8:] =', name[8:])        # huhu

# Tách string => trả về danh sách: split()
    # Mặc định tách khi gặp khoảng trắng
str1 = '1 2 3 4 5 6 7 8 9'
arr1 = str1.split()
print('arr1 =', arr1)      

str2 = 'Duc Huy choi game trong gio'
arr2 = str2.split()
print('arr2 =', arr2)

    # Tách khi gặp ký tự bất kì
str3 = 'a,b,c,d,e,f,g,h,i'
arr3 = str3.split(',')
print('arr3 =', arr3)

str4 = 'x-y-z-a-b-c-d-e-f'
arr4 = str4.split('-')
print('arr4 =', arr4)

# Xóa khoảng trắng ở đầu và cuối string: strip()
name = '     Bao Phuc     '
print('Trước strip():', name)
name = name.strip()
print('Sau strip():', name)

# Thay thế substring: replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ: replace(old, new)
song2 = song.replace('doo', 'phong')
print('song2 =', song2)
    # Thay thế 1 phần: replace(old, new, count)
song3 = song.replace('doo', 'huy', 3)
print('song3 =', song3)

# Kết hợp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
    # Kết hợp với khoảng trắng
str1 = ' '.join(arr)
print('str1 =', str1)
    # Viết liền
str2 = ''.join(arr)
print('str2 =', str2)
    # Kết hợp với ký tự bất kì
str3 = '-'.join(arr)
print('str3 =', str3)

# Chuẩn hóa string
name = 'nGuYeN gIa lInH'
    # Viết hoa tất cả: upper()
print('Viết hoa:', name.upper())
    # Viết thường tất cả: lower()
print('Viết thường:', name.lower())
    # Viết hoa chữ cái đầu: title()
print('Viết hoa chữ cái đầu:', name.title())

# Ví dụ: x - tên gốc, y - input tìm kiếm
x = 'MindX Technology School'
y = 'mindx'
print('x == y', x == y)      # False
print('y.lower() in x.lower():', y.lower() in x.lower())     