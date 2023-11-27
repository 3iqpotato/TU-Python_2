


class Animal:
    def __init__(self, age):
        self.__age = self.set_age(age)

    # @property
    # def age(self):
    #     return self.__age
    #
    #
    # @age.setter
    # def age(self, age):
    #     if age > 0:
    #         self.__age = age
    #     else:
    #         self.__age = 0


    def talk(self):
        print('I cant talk')

    def move(self):
        print('I cant move')

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
             self.__age = age
             return age
        else:
             self.__age = 0
             return 0

    def __str__(self):
        return f"Animal is {self.__age} years old."

class GoldFish(Animal):
    def __init__(self, age, type):
        super().__init__(age)
        self.type = type

    def talk(self):
        print('tell me your wishes')

    def move(self):
        print('I can swim')

g = GoldFish(20, 'fish')
g.get_age()
print(g)
g.set_age(g.get_age() + 1)

print(g)
print()

class Dog(Animal):
    def __init__(self, age, type):
        super().__init__(age)
        self.type = type

    def talk(self):
        print('bla bal bal')

    def move(self):
        print('I can run')

d = Dog(-10, 'dog')
d.move()
d.talk()
print(d)
print()
class Carp(Animal):
    def __init__(self, age, type):
        super().__init__(age)
        self.type = type

    def move(self):
        print('I can swim')

carp = Carp(10, 'riba')
carp.move()
carp.talk()
print(carp)
print()
class Duck(Animal):
    def __init__(self,age, type):
        super().__init__(age)
        self.type = type

    def talk(self):
        print('ap pa pa pa')

    def move(self):
        print('I can walk')


duck = Duck(18,'duck')
duck.talk()
duck.move()
print(duck)