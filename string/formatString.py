# 根据指定的宽度打印格式良好的价格列表

width = int (input("Enter the width: "))
prince_width = 10
item_width = width - prince_width
header_format = "{{:{}}}{{:>{}}}".format(item_width,prince_width)
fmt = "{{:{}}}{{:>{}.2f}}".format(item_width,prince_width)
print('='*width)
print(header_format.format("Item","Price"))
print('-'*width)
print(fmt.format("Apple", 0.4))
print(fmt.format("Banana", 0.5))
print(fmt.format("Orange", 1.92))
print(fmt.format("Pineapple(16 oz.)", 2.8))
print(fmt.format("Grapes(4 lbs.)", 12))

print('='*width)
