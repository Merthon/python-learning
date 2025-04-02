def my_decorator(func):
    def wrapper():
        print("在函数调用前执行一些操作")
        func()  # 调用原始函数
        print("在函数调用后执行一些操作")
    return wrapper

@my_decorator
def say_hello():
    print("你好")

# 调用函数
say_hello()