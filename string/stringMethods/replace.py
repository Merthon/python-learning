#方法：replace()将字符串中的指定子串替换成另一个子串。
s = "hello world"
print(s.replace("l", "L")) #输出：heLLo worLd   
#如果要替换所有子串，可以将第二个参数设为空字符串。
print(s.replace("l", "")) #输出：heo word   