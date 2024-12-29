# setdefault方法有点像get方法，
# 但是如果字典中不存在指定的键，则会将默认值添加到字典中并返回。
d = {}
d.setdefault('a', 1)
print(d)  # {'a': 1}
d.setdefault('a', 2)
print(d)  # {'a': 1}
d.setdefault('b', 3)
print(d)  # {'a': 1, 'b': 3}