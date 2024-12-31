# json 标准模块采用 Python 数据层次结构，
# 并将之转换为字符串表示形式；
# 这个过程称为 serializing （序列化）。
import json

x = [1,'simple','list']
str = json.dumps(x) # 将列表 x 转换为 JSON 字符串
print(str)
# Output: '[1, "simple", "list"]'