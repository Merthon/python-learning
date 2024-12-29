# 使用函数dict从其他映射或者键值对序列创建字典
items = [('name', 'Alice'), ('age', 25), ('city', 'Beijing')]
d = dict(items)
print(d)  
# {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(d['name'])
# Alice
# 还可以使用关键字实参来调用这个函数
d = dict(name='Alice', age=25, city='Beijing')
print(d)  
# {'name': 'Alice', 'age': 25, 'city': 'Beijing'}