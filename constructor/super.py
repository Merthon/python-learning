# 重写方法
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaaah ...")
            self.hungry = False
        else:
            print("No thanks")
# 使用这个类
# b = Bird()
# b.eat() # Aaaaah ...
# b.eat() # No thanks

# 增加一个子类
class SongBird(Bird):
    def __init__(self):
        super().__init__()# 调用父类的构造函数
        self.sound = "Chirp chirp"
    def sing(self):
        print(self.sound)
# 使用这个子类
s = SongBird()
s.sing() # Chirp chirp
#s.eat()
# AttributeError: 'SongBird' object has no attribute 'hungry'
s.eat() # Aaaaah ...
s.eat() # No thanks
