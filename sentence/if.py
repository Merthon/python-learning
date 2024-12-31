# if-else 语句 
'''
  name = input("Please enter your name: ")
if name.endswith("Gao"):
    print("Hello, Mr. Gao!")
else:
    print("Hello, " + name + "!")  
      # 注意这里的字符串拼接
'''
mood_index =int(input("请输入数字："))
if mood_index >= 90:
    print("good!")
elif mood_index >= 60:
    print("not bad!")
else:
    print("so-so...")