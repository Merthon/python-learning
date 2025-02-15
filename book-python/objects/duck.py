class Duck:
    def __init__(self, name):
        self.name = name
    def quack(self):
        print(f"I'm {self.name}!")

def main():
    star = Duck('star')
    star.quack()

if __name__ == "__main__":
    main()