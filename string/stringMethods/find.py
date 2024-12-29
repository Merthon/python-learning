# 方法find()用于查找字符串中子串的位置
# 找到返回子串的第一个字符的索引
# 如果没有找到，则返回-1

string = "Hello,world!"
substring = "world"

index = string.find(substring)

if index == -1:
    print("Substring not found.")
else:
    print("Substring found at index:", index) 

# Output: Substring found at index: 6 

