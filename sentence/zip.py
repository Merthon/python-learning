# 并行遍历 内置函数zip()
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
for name, age in zip(names, ages):
    print(name, age)
# Alice 25
# Bob 30
# Charlie 35   
# 注意：zip()函数返回的是一个迭代器对象，
# 需要用list()函数转换为列表才能查看其内容。