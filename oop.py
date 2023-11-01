import random


class Animal():
    _count = 0
    force = 1

    def __init__(self, name, weight, color):
        self.__name = name
        self.weight = weight
        self.color = color
        self.fullness = 0
        Animal._count += 1

    def eat(self):
        print(f"{self.__name} поел")
        self.fullness += 1

    def __str__(self):
        return f"Животное {self.__name}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def say(self):
        print(f"{self.__name} говорит!")


    @staticmethod
    def get_count():
        return Animal._count

    def __add__(self, other):
        if self.force > other.force:
            winner_name = self.get_name()
        elif self.force < other.force:
            winner_name = other.get_name()
        else:
            selected = random.choice([self, other])
            winner_name = selected.get_name()
        print("победил", winner_name)


class Cat(Animal):
    force = 2

    def __str__(self):
        return f"Кот {self.get_name()}"

    def say(self):
        print(f"{self.get_name()} мяу!")

    def mur(self):
        print(f"{self.get_name()} мур!")


vasya = Cat("Вася", 5, "black")
barsik = Cat("Барсик", 8, "ginger")
print(vasya)
parrot = Animal("Кеша", 3, "red")
print(parrot + barsik)


class Device():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Phone(Device):
    def make_a_call(self, phone_number):
        print(f"Звоним на {phone_number}")

    def take_a_photo(self):
        print(f"{self.name} фотография")

class PhotoCamera(Device):
    def take_video(self):
        print("записывает видео")

    def take_a_photo(self):
        print(f"{self.name} фотография")