# del语句用于删除列表、字典或集合中的元素。
x = ["Hello","World"]
y = x
y[1] = "Python"
print(x) # Output: ['Hello', 'Python']
print(y) # Output: ['Hello', 'Python']

del x
print(y) # Output: ['Hello', 'Python']

# 注意：del语句只能删除列表、字典或集合中的元素，不能删除变量。