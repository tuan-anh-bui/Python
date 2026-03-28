
import time

try:
    nam_sinh = int(input("Nhập năm sinh của bạn: "))
    
    # Lấy năm hiện tại
    x = time.localtime()
    year = x[0]
    
    # Tính tuổi
    tuoi = year - nam_sinh
    
    if tuoi >= 0:
        print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")
    else:
        print("Năm sinh không thể lớn hơn năm hiện tại.")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập một số nguyên.")
