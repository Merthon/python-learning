# 捕获异常，可以使用try/except语句。
# 实例
try:
    x = int (input("Enter the first number: "))
    y = int (input("Enter the second number: "))
    print(x/y)
    # the following line will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: division by zero!")