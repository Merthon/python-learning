# 一个简单的数据库 
# 字典包含键‘phone’和‘addr’，分别对应电话号码和地址。

people = {
    'Alice':{
        'phone': '1234567890',
        'addr': '123 Main St'
    },
    'Bob':{
        'phone': '9876543210',
        'addr': '456 Oak Ave'   
    },
    'Charlie':{
        'phone': '5555555555',
        'addr': '789 Elm St'
    }
}

# 电话号码和地址的描述性标签，用于打印输出
labels = {
    'phone': 'Phone Number',
    'addr': 'Address'
}
name = input('Enter a name: ')

# 要查询电话号码还是地址
request = input('Phone number(p) or address(a)? ')

# 使用正确的键：
if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'addr'
else:
    print('Invalid input.')
    exit()

# 仅当输入的名字存在于字典中时才打印信息
if name in people:
    print("{}'s {}: {}".format(name, labels[key], people[name][key]))
else:
    print('Name not found.')

