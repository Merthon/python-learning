# 读取文件内容
f = open('/Users/chenx/Workspace/Python/file/somefile.txt','r')

# read(n)
#print(f.read(7))
#print(f.read(5))

# 读取全部内容
#print(f.read())  

# 读取一行
print(f.readline())

# 关闭文件
f.close()