# join是一个字符串方法，用于将序列中的元素以指定的字符连接成一个新的字符串。
# 用法与split方法类似，但join方法的第一个参数是序列，第二个参数是用于连接的字符。

s = ['a', 'b', 'c', 'd']
result = s.join(s) 
print(result) # Output: 'abcd'  

result = s.join('-') 
print(result) # Output: 'a-b-c-d' 
