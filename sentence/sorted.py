# sorted函数是Python内置的函数，
# 它可以对一个可迭代对象进行排序，
# 并返回一个新的排序后的列表。

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 按升序排序
sorted_lst = sorted(lst)
print(sorted_lst)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# 按降序排序
sorted_lst = sorted(lst, reverse=True)
print(sorted_lst)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# 按自定义函数排序
sorted_lst = sorted(lst, key=lambda x: -x)
print(sorted_lst)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]