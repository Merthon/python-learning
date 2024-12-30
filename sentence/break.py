# 跳出循环
from math import sqrt

for i in range(99, 0, -1):
    root = sqrt(i)
    if root == int(root):
        print(i)
        break
# 输出：9   
# 循环中使用了 break 语句，跳出了循环，并输出了满足条件的数字 9。