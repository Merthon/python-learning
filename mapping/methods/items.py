# 方法items返回一个包含所有字典项的列表，每个项由键值对组成。
d = {'a': 1, 'b': 2, 'c': 3}
print(d.items()) 
 # [('a', 1), ('b', 2), ('c', 3)]
# 也可以使用for循环遍历字典项：
for key, value in d.items():
    print(key, value)  # a 1 b 2 c 3    