# 方法clear()用于清空列表或字典中的元素。
d = {}
d['name'] = 'chen'
d['age'] = 25
d['city'] = 'Beijing'
print(d)
returned_value = d.clear()
print(d)
print(returned_value) # None