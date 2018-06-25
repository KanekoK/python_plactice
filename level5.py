# 1, 2, 3, 5, 7, 11, 13
# 偶数ではない、しかし2は例外

from math import sqrt
for i in range(2, 5000):
    if 0 not in [i%j for j in range(2, int(sqrt(i))+1)]:
        print(i)
