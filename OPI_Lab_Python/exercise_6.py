class Apple:
    def __init__(self, kind, taste):

        self.kind = kind
        self.color = 'green'
        self.taste = taste

    def get_ready_to_be_eaten(self):
        if self.kind == 'golden':
            self.color = 'yellow'
        elif self.kind == 'devil':
            self.color = 'purple'

apple = Apple('golden', 'kisela')





class Animal:
    def __init__(self):
        pass

    def talk(self):
        print("I don't talk")

    def move(self):
        print("I don't move")



class Cat(Animal):
    def __init__(self, type):
        super(Cat, self).__init__()
        self.type = type

    def talk(self):
        print('mql mql mql mql mql mql mql mql mql mql mql')
    def move(self):
        print("I can move")

c = Cat('kotka')
c.talk()
c.move()
#
# class Fishes(Animal):
#     def __init__(self, type):
#         super().__init__()
#         self.type = type
class Dog(Animal):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def talk(self):
        print('bla bal bal')

    def move(self):
        print('I can run')

d = Dog('dog')
d.move()
d.talk()
class Carp(Animal):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def move(self):
        print('I can swim')

carp = Carp('riba')
carp.move()
carp.talk()
class Duck(Animal):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def talk(self):
        print('ap pa pa pa')

    def move(self):
        print('I can walk')


duck = Duck('duck')
d.talk()
d.move()
class GoldenFish(Animal):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def move(self):
        print('I can swim')

    def talk(self):
        print('Tell me your wishes')

g_fish = GoldenFish('goldfihs')
g_fish.talk()
g_fish.move()