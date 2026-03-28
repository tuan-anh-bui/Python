

try:
    n = int(input("Nhập vào một số nguyên dương: "))
    if n > 0:
        if n % 2 == 0:
            print("Đây là một số chẵn")
        else:
            print("Đây là một số lẻ")
    else:
        print("Vui lòng nhập một số nguyên dương.")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập một số nguyên.")
