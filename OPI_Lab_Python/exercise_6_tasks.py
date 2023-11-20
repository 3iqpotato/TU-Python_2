class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print_name(self):
        print(self.name, self.nationality)

gogo = Person('Gogo', 'Lazarov', 90, 'Bulgarian')

gogo.print_name()
class Human:
    def __init__(self, code):
        self.code = code


class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.year_of_study = year_of_study

    def print_name(self):
        print(self.name, self.nationality, self.university, self.year_of_study)

pepi = Student('pepi', 'Gogo', 90, 'Bulgarian', 'Tu', 1)

pepi.print_name()

class Lecture(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super(Lecture, self).__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print_name(self):
        print(self.name, self.nationality, self.university, self.experience)


bob = Lecture('BOB', 'Bobov', 89, 'Bulgarian', 'Tu', 90)
bob.print_name()

def generate_vector(n, my_vector):
    if n == len(my_vector):
        print(''.join(str(x) for x in my_vector))
        return
    for number in range(0, 2):
        my_vector[n] = number
        generate_vector(n+1, my_vector)

#tova ne go pishi
class SuperHuman(Human, Person):
    def __init__(self, name, nationality, age, family, code):
        Person.__init__(self, name, family, age, nationality)
        Human.__init__(self, code)

lazar = SuperHuman('laci', 'Bg', 99, 'Nqkakwa', '456789')
print(lazar.code)
print(lazar.name)



# num = int(input('enter num'))
# my_vector = [0, 0, 0, 0, 0, 0]
# generate_vector(num, my_vector)
