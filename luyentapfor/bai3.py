# Bài 3: In ra các số trong khoảng từ 80 - 100 thỏa mãn điều kiện vừa chia hết cho 2, vừa chia hết cho 3.

import sys

# Đảm bảo in ra tiếng Việt không bị lỗi encoding trên một số môi trường
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# In các số từ 80 đến 100 (bao gồm 100)
for i in range(80, 101):
    # Điều kiện vừa chia hết cho 2 vừa chia hết cho 3 (chia hết cho 6)
    if i % 2 == 0 and i % 3 == 0:
        print(i)
