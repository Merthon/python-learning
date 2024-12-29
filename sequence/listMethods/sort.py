# sort方法用于对列表进行排序，默认是升序排序。

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lst.sort()
print(lst)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# 也可以指定排序的方向，reverse=True表示降序排序。
lst.sort(reverse=True)
print(lst)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1] 

# 如果要自定义排序规则，可以传入一个函数作为参数。
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lst.sort(key=lambda x: x % 2)  # 按照元素的奇偶性进行排序
print(lst)  # [1, 1, 3, 3, 4, 5, 5, 5, 6, 9, 2] 