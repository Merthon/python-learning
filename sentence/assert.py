# 断言 assert 语句用于在运行时验证程序的状态，如果断言失败，程序会抛出 AssertionError 异常。
age = 20
assert 0 < age < 100
age = -1
assert 0 < age < 100    
# 运行结果：
# Traceback (most recent call last):
#   File "assert.py", line 4, in <module>
#     assert 0 < age < 100
# AssertionError