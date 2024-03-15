class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} сел(а).")

    def roll_over(self):
        print(f"{self.name} перекатывается.")


my_dog = Dog('Willie', 6)
print(f"Имя собаки: {my_dog.name}")
print(f"Возраст собаки: {my_dog.age}")

my_dog.sit()
my_dog.roll_over()

second_dog = Dog('Lucy', 3)
print(f"\nИмя второй собаки: {second_dog.name}")
print(f"Возраст второй собаки: {second_dog.age}")

second_dog.sit()
second_dog.roll_over()
