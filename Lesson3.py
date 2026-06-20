# ===================== Luyện tập =====================
# Câu 1: Nhập một số từ bàn phím và in ra số đó.
number = input("Nhập một số: ")
print("Số bạn vừa nhập là:", number)

# Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.
number = int(input('Nhập 1 số nguyên: '))
if number % 2 == 0:
    print(number, "là số chẵn")
else:
    print(number, "là số lẻ")

# Câu 3: Viết chương trình tính tổng, hiệu, tích, thương, chia lấy nguyên, chia lấy dư, lũy thừa của hai số nhập từ bàn phím.
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

print('Tổng:', a + b)
print('Hiệu:', a - b)
print('Tích:', a * b)
print('Thương:', a / b)
print('Chia lấy nguyên:', a // b)
print('Chia lấy dư:', a % b)
print('Lũy thừa:', a ** b)

# Câu 4: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).
usd = float(input("Nhập số tiền USD: "))
vnd = usd * 27000
print(f'${usd} = {vnd} VND')

# Bài 5: Nhập số điện bạn sử dụng (kWh)
# Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# Bậc 1:    0kWh - 50kWh           giá 1.8k VND / kWh
# Bậc 2:    51kWh - 100kWh         giá 2k VND / kWh
# Bậc 3:    101kWh - 200kWh        giá 2.3k VND / kWh
# Bậc 4:    trên 201kWh            giá 3k VND / kWh

# Nhập số điện sử dụng
kwh = float(input("Nhập số điện sử dụng (kWh): "))

# Biến để lưu tổng tiền điện
money = 0

# Tính tiền điện
if 0 <= kwh <= 50:
    money = kwh * 1800
elif 50 < kwh <= 100:
    money = 50 * 1800 + (kwh - 50) * 2000
elif 100 < kwh <= 200:
    money = 50 * 1800 + 50 * 2000 + (kwh - 100) * 2300
elif kwh > 200:
    money = 50 * 1800 + 50 * 2000 + 100 * 2300 + (kwh - 200) * 3000
else:
    print("Số điện sử dụng không hợp lệ.")

# Hiển thị kết quả
print(f'Tiền điện phải trả: {money} VND')

# Bài 6: Nhập số giây
# yêu cầu: Chuyển sang định dạng giờ phút giây
# VD: 3661s = 1h 1m 1s

# Nhập số giây
time = int(input("Nhập số giây: "))

# Chuyển đổi
hour = time // 3600
minute = (time % 3600) // 60
second = time % 60

# Hiển thị kết quả
print(f'{time}s = {hour}h {minute}m {second}s')

# Bài 7: Chia m cái kẹo cho n học sinh
# Yêu cầu:
    # Nhập m, n từ bàn phím
    # Tính số kẹo mỗi học sinh được nhận
    # Tính số kẹo còn lại sau khi chia

# Nhập dữ liệu
m = int(input("Nhập số lượng kẹo: "))
n = int(input("Nhập số lượng học sinh: "))

# Hiển thị kết quả
print('Số kẹo học sinh nhận được:', m // n)
print('Số kẹo còn thừa:', m % n)