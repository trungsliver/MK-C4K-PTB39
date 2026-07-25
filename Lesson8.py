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