# 发现某个方法不需要使用当前实例里的任何内容，
# 那可以使用@staticmethod来定义一个静态方法。
import random

class Cat:
    def __init__(self, name):
        self.name = name
    def say(self):
        sound = self.get_sound()
        print(f'{self.name}: {sound}...')
    @staticmethod
    def get_sound():
        repeats = random.randrange(1,10)
        return ''.join(['Meow'] * repeats)