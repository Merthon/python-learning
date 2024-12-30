# finally子句
x = None
try:
    x = 1 / 0
finally:
    print("CLeaning up ...")
    del x
    # Output: CLeaning up ...