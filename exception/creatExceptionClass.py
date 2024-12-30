# 创建异常类，要直接或者间接继承自Exception类

class SomeException(Exception):pass

# 创建一个继承自SomeException的子类
class AnotherException(SomeException):pass

# 创建一个继承自AnotherException的子类
class YetAnotherException(AnotherException):pass