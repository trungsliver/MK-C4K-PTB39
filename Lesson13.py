# ================ ÔN TẬP ================

# Biến số: 
    # Công dụng: dùng để lưu trữ dữ liệu
    # Đặc điểm: có thể thay đổi khi lập trình

# Các quy tắc đặt tên biến:
    # Chỉ gồm chữ cái tiếng anh, số và dấu _
    # Không được bắt đầu bằng số
    # Không trùng với từ khóa của Python

# 2 cách đặt tên phổ biến:
    # camelCase: myVariableName
    # snake_case: my_variable_name

# 4 cách hiển thị dữ liệu:
    # Cách 1: dùng dấu + 
    # Cách 2: dùng dấu ,
    # Cách 3: dùng f-string
    # Cách 4: dùng """ """

# Data Types - Kiểu dữ liệu: string, int, float, bool/boolean
    # Hàm kiểm tra kiểu dữ liệu: type()

# Operators - Toán tử:
    # Toán tử số học: +, -, *, /, //, %, **
    # Toán tử so sánh: ==, !=, >, <, >=, <=
    # Toán tử logic: and, or, not

# Conditions statement - Câu điều kiện:
    # Dạng thiếu: if 
    # Dạng đủ: if - else
    # Dạng đa nhánh: if - elif - ... - else
    # match - case 

# Vòng lặp for - Vòng lặp hữu hạn:
    # range(start, stop, step):
    # VD: for i in range(5):  # start = 0, stop = 5, step = 1

# Vòng lặp while - Vòng lặp vô hạn:
    # while <điều kiện>:
    # Lặp cho đến khi điều kiện sai

# Câu lệnh điều khiển vòng lặp:
    # break: dừng vòng lặp, bỏ qua các lần lặp còn lại
    # continue: bỏ qua lần lặp hiện tại, tiếp tục vòng lặp

# Xử lý lỗi: try - except

# Danh sách: array - List
    # Create: arr = [], arr = [1,2,3]
    # Read:
        # len(arr) - độ dài danh sách
        # arr[index] - truy xuất phần tử theo index
        # Duyệt danh sách:
            # Cách 1 (Dùng cả index và value):  for i in range(len(arr))
            # Cách 2 (Dùng value):              for item in arr
            # Cách 3 (Dùng hàm có sẵn):         for index, value in enumerate(arr)
    # Update:
        # append(value)         - thêm phần tử vào cuối danh sách
        # insert(index, value)  - thêm phần tử vào vị trí index
        # arr[index] = value    - thay đổi giá trị phần tử 
    # Delete:
        # pop(index)        - xóa phần tử theo index
        # remove(value)     - xóa phần tử theo giá trị
        # clear()           - xóa tất cả phần tử trong danh sách
    # Các hàm có sẵn:
        # arr.sort(reverse=True/False) - sắp xếp danh sách
        # min(arr) - tìm phần tử nhỏ nhất
        # max(arr) - tìm phần tử lớn nhất

# String methods - Các phương thức xử lý chuỗi:
    # Duyệt string (giống danh sách)
    # substring: xâu con: 
    # slicing (cắt chuỗi): string[start:stop:step]
    # split (tách) => trả về danh sách
    # replace: thay thế
    # strip: xóa khoảng trắng đầu cuối
    # join: nối chuỗi
    # CHuẩn hóa: lower, upper, title

# Functions - Hàm:
    # Hàm không có tham số:
    # Hàm có tham số:
    # Hàm có giá trị trả về: