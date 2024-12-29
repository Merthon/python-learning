# 检查用户名和PIN码
# 要检查特定的值是否在序列中，可以用运算符in来判断。

database = [
    ['user1','1234'],
    ['user2','5678'],
    ['user3','9012'],
    ['user4','3456']
]
username = input("User name:")
pin = input("PIN code:")

if [username, pin] in database:
    print("success")
else:
    print("failed")