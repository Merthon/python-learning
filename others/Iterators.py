class MyIterator:
    def __init__(self, date):
        self.date = date   # 数据容器
        self.index = 0    # 当前索引

    def __iter__(self):
        return self   # 返回迭代器本身
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  # 结束迭代
        
# 使用迭代器
my_iter = MyIterator([1, 2, 3, 4])
for item in my_iter:
    print(item)