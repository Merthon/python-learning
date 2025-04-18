# 创建和使用字典映射
# 字典映射是一种常见的数据结构，它将一个值映射到另一个值。
# 在Python中，字典映射可以用字典来实现。
# 字典映射的创建方法很简单，只需要将键值对放入一个字典中即可。

# 示例：
# 创建一个字典映射，将英文单词映射到中文翻译
word_map = {
    "apple": "苹果",
    "banana": "香蕉",
    "orange": "橘子",
    "grape": "葡萄",
    "pear": "梨"
}

# 使用字典映射
# 字典映射的使用方法也很简单，只需要通过键来获取对应的值即可。
# 示例：
# 假设我们要翻译英文单词"apple"为中文，可以用如下代码：
print(word_map["apple"])  # 输出：苹果

# 字典映射的优点是可以快速查找对应的值
# 缺点是不方便添加和修改映射关系。
# 如果需要修改映射关系，需要重新创建字典，代价较大。