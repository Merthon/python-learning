# %s是转换说明符，指出了要替换的位置。这里，%s表示要替换成字符串。
format = "Hello, %s.%s enough for ya?"
values = ("world", "Hot")
result = format % values
print(result)   
# Output: Hello, world.Hot enough for ya?