# 创建类时，可以定义一个 __init__ 方法，该方法在对象被创建时自动调用。
# __init__ 方法可以有参数，这些参数在创建对象时传递给 __init__ 方法。
# __init__ 方法的作用是为对象初始化属性。

class TheFirstDemo:
    '''这是定义python的第一个类'''
    def __init__(self):
        print("调用构造方法")
    # 定义一个类属性
    add = "https://www.baidu.com"
    # 定义了一个say方法
    def say(self,content):
        print(content)
# 创建对象
obj = TheFirstDemo()