# 方法：index()在列表中查找指定元素的第一个出现的索引位置

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 查找元素1的第一个出现的索引位置
print(list1.index(1))  # Output: 0

# 查找元素10的第一个出现的索引位置
print(list1.index(10))  # Output: 9

# 查找元素11的第一个出现的索引位置，如果不存在，则会引发ValueError异常
# print(list1.index(11))  # Output: ValueError: 11 is not in list