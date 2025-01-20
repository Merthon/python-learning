class Restaurant :
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_res(self):
        print(f"name s {self.restaurant_name}")
        print(f"name s {self.cuisine_type}")

    def open_res(self):
        print("res is opening")

res = Restaurant('star', 'hot pat')
res.describe_res()
res.open_res()