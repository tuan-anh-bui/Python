
try:
    a = int(input("Nhập cạnh a: "))
    b = int(input("Nhập cạnh b: "))
    c = int(input("Nhập cạnh c: "))

    if a > 0 and b > 0 and c > 0:
        if (a + b > c) and (a + c > b) and (b + c > a):
            print("Độ dài ba cạnh tam giác")
        else:
            print("Đây không phải độ dài ba cạnh tam giác")
    else:
        print("Vui lòng nhập các số nguyên dương.")
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập các số nguyên.")
