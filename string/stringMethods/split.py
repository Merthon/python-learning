# split是字符串方法，其作用与join相反
# 该方法可以将字符串拆分为序列

s = "hello world"

# 按空格分割
result = s.split()
print(result)  # ['hello', 'world']

# 按指定字符分割
result = s.split('l')
print(result)  # ['he', 'o world']

# 注意：如果分割的字符不存在于字符串中，则返回整个字符串作为一个元素