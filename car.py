Eclass Car():
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)

my_car = Car("Toyota")
my_car.get_brand()
