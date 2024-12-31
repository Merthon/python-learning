# re 模块为高级字符串处理提供正则表达式工具。
# 对于复杂的匹配和操作，正则表达式提供简洁
import re
# 匹配字符串
pattern = r'hello'
string = 'hello world'
match = re.search(pattern, string)
if match:
    print('Match found:', match.group())
else:
    print('Match not found')

# 匹配字符串并替换
pattern = r'world'
string = 'hello world'
new_string = re.sub(pattern, 'Python', string)
print(new_string)
