# 创建自定义类
class Person:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello, my name is{}.".format(self.name))

# 创建实例对象
foo = Person()
bar = Person()
foo.set_name("Luke Walker")
bar.set_name("John Doe")

# 调用方法
foo.greet()
bar.greet() 

# 输出结果：
# Hello, my name is Luke Walker.
# Hello, my name is John Doe.