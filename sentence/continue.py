# continue是Python中的一个关键字，
# 用于跳过当前循环的剩余语句，并直接开始下一轮循环。
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 输出结果：
# 1
# 2
# 4
# 5