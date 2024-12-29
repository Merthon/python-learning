# 方法：extend()可以同时添加多个元素到列表中。

# 语法：list.extend(iterable)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)  # Output: [1, 2, 3, 4, 5, 6]
# 注意：extend()方法不会修改原列表，而是返回一个新的列表。