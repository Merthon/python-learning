# glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数:
import glob

# 使用 glob 模块搜索当前目录下所有以.txt 结尾的文件:
file_list = glob.glob('*.txt')
print(file_list)
