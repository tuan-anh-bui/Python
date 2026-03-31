# Bài 4: Nhập vào 1 số nguyên n < 20 từ bàn phím.
# In ra các số thỏa mãn điều kiện chia hết cho 5 hoặc chia hết cho 7.
# Ở đây tôi giả định là in các số từ 1 đến n (thường các bài tập loại này yêu cầu in trong phạm vi n).

import sys

# Đảm bảo in ra tiếng Việt không bị lỗi encoding trên một số môi trường
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    n = int(input("Nhập vào số nguyên n (n < 20): "))
    
    # In ra các số từ 1 đến n thỏa mãn điều kiện chia hết cho 5 hoặc 7
    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            print(i)
except ValueError:
    print("Vui lòng nhập một số nguyên.")
except EOFError:
    pass
