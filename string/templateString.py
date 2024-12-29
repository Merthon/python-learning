from string import Template
# 模板字符串
# 定义模板字符串，其中$name表示占位符
# substitute()方法用于替换模板字符串中的占位符  
template = Template('Hello, $name!')
tmpl = template.substitute(name='World')
print(tmpl)   # Output: Hello, World!