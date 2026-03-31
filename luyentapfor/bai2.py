# Bài 2: Nhập vào 1 số nguyên n từ bàn phím.
# Nếu số đó lớn hơn 10 thì in ra dòng text: Số nhập vào phải bé hơn 10.
# Nếu số đó nhỏ hơn hoặc bằng 10: In ra những số chẵn trong khoảng từ 1 đến n.

import sys

# Đảm bảo in ra tiếng Việt không bị lỗi encoding trên một số môi trường
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    n = int(input("Nhập vào số nguyên n: "))
    
    if n > 10:
        print("Số nhập vào phải bé hơn 10.")
    else:
        # In các số chẵn trong khoảng từ 1 đến n
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)
except ValueError:
    print("Vui lòng nhập một số nguyên.")
except EOFError:
    pass
