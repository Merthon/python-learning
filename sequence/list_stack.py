#使用列表方法实现堆栈非常容易
# 最后插入的最先取出（“后进先出”）。
# 把元素添加到堆栈的顶端，使用 append() 。
# 从堆栈顶部取出元素，使用 pop() ，不用指定索引。
stack = [3,4,5]
old_list =stack.append(6)
print(stack) # [3, 4, 5, 6]
old_list = stack.pop()
print(stack) # [3, 4, 5]
print(old_list) # 6