class Animal:
    def __init__(self, age):
        self.age = age

    def talk(self):
        print('I cant talk')

    def move(self):
        print('I cant move')

    def get_age(self):
        print(self.age)

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"Animal is {self.age} years old."