# 方法remove()用于删除列表中第一个为指定值的元素。如果没有找到指定值，则会引发ValueError异常。

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 删除第一个值为3的元素
lst.remove(3)
print(lst)  # [1, 2, 4, 5, 6, 7, 8, 9]

# 删除第一个值为10的元素，会引发ValueError异常
lst.remove(10)      
 # ValueError: list.remove(x): x not in list