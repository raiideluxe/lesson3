class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


class Human:
    default_name = "John Doe"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.money = 0
        self.house = None

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, House: {self.house}, Money: {self.money}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}, Default Age: {Human.default_age}")

    def make_deal(self, house, price):
        if self.money >= price:
            self.money -= price
            self.house = house
            print(f"{self.name} bought a house!")
        else:
            print("Not enough money to buy the house!")

    def earn_money(self, amount):
        self.money += amount

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.money >= final_price:
            self.make_deal(house, final_price)
        else:
            print("Not enough money to buy the house!")

Human.default_info()

person = Human("Alice", 25)
person.info()

small_house = SmallHouse(50000)
person.buy_house(small_house, 10000)
person.info()

person.earn_money(60000)
person.buy_house(small_house, 10000)
person.info()
