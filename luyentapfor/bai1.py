# Bài 1: Nhập vào số nguyên n từ bàn phím. In ra tích của 2 nhân với các giá trị nhỏ hơn n.
# Ví dụ: Nhập n = 4 thì in ra 2 = 2*1, 4 = 2*2, 6 = 2*3.

import sys

# Đảm bảo in ra tiếng Việt không bị lỗi encoding trên một số môi trường
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    n = int(input("Nhập vào số nguyên n: "))
    # In ra tích của 2 với các giá trị nhỏ hơn n (từ 1 đến n-1)
    results = []
    for i in range(1, n):
        results.append(f"{2 * i} = 2*{i}")
    
    # In kết quả trên một dòng hoặc tùy ý, ở đây tôi in theo ví dụ
    print(", ".join(results))
except ValueError:
    print("Vui lòng nhập một số nguyên.")
except EOFError:
    pass
