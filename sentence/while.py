# 在条件何时结束未知的情况下，while比for循环更加灵活。
# 计算平均值
total = 0
count = 0
user_input = input("请输入数字（输入完成所有数字以后输入done）：")
while user_input!= "done":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("请输入数字（输入完成所有数字以后输入done）：")
if count == 0:
    print("没有输入任何数字")
else:
    result = total / count
print("平均值是：", result)