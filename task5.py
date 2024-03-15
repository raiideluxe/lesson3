class Nikola:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        if name != 'Николай':
            self.name = f'Я не {name}, а Николай'
        else:
            self.name = 'Николай'
        self.age = age

# Тесты
person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)

print(person1.name)  # Выведет: Я не Иван, а Николай
print(person2.name)  # Выведет: Николай

# Попытка добавить новый атрибут 'surname' к объекту person2 приведет к ошибке
"""person2.surname = 'Петров' """
