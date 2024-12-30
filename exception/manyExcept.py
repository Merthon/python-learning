# 多个异常捕获

try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("division by zero!")
except NameError:
    print("name error!")
except:
    print("unknown error!")  # 捕获所有其他异常