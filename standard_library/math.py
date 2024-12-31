# math 模块提供对浮点数学的底层C库函数的访问:
import math

# 常量
print(math.pi)  # 圆周率
print(math.e)  # 自然常数
# random 模块提供用于生成随机数的函数
import random

# 随机数
print(random.random())  # 0-1之间的随机数
print(random.randint(1, 10))  # 1-10之间的随机整数

# statistics 模块提供用于计算数学统计学的函数
import statistics

# 平均值
print(statistics.mean([1, 2, 3, 4, 5]))  # 3.0
# 中位数
print(statistics.median([1, 2, 3, 4, 5]))  # 3.0
# 众数
print(statistics.mode([1, 2, 3, 4, 5, 5]))  # 5
# 方差
print(statistics.variance([1, 2, 3, 4, 5]))  # 1.25
