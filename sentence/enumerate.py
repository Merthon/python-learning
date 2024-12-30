# 内置函数enumerate()可以将一个可迭代对象（如列表、元组、字符串）组合为一个索引序列，
# 同时列出每个元素的索引位置。
for index, value in enumerate(['apple', 'banana', 'orange']):
    print(index, value) 
# 输出：
# 0 apple
# 1 banana
# 2 orange  