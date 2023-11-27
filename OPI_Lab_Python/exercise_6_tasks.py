class Person:
    def __init__(self, name, family, age, nationality):
        self.set_atributes(name, family, age, nationality)
        # self.name = name
        # self.family = family
        # self.age = age
        # self.nationality = nationality

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            self.__age = 0
        else:
            self.__age = value
    def set_age(self, age):
        if age < 0:
            self.age = 0
            return 0
        else:
            self.age = age
            return age

    def set_atributes(self, name, family, age, nationality):
        if name == '':
            self.name = 'Invalid'
        else:
            self.name = name
        if family == '':
            self.family = 'Invalid'
        else:
            self.family = family
        if age == '':
            self.age = 'Invalid'
        else:
            self.age = age
        if nationality == '':
            self.nationality = 'Invalid'
        else:
            self.nationality = nationality


    def print_name(self):
        return f"{self.name}, {self.family}, {self.nationality}, {self.age}"

gogo = Person('FOFO', 'Lazarov', 10, 'Bulgarian')
print(gogo.print_name())


class Student(Person):
    def __init__(self, name, family, age, nationality, university, year_of_study):
        super().__init__(name, family, age, nationality)
        self.set_new_atributes(university, year_of_study)

    def set_new_atributes(self, university, year_of_study):
        if university == '':
            self.university = "Invalid"
        else:
            self.university = university
        if year_of_study == '':
            self.year_of_study = 'Invalid'
        else:
            self.year_of_study = year_of_study



    def print_name(self):
        return f"{super(Student,self).print_name()}, {self.university}, {self.year_of_study}"

pepi = Student('pepi', 'Gogo', 90, 'Bulgarian', 'Tu', 1)

print(pepi.print_name())

class Lecture(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super(Lecture, self).__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print_name(self):
        return f"{super(Lecture,self).print_name()}, {self.university}, {self.experience}"


bob = Lecture('BOB', 'Bobov', 89, 'Bulgarian', 'Tu', 90)
print(bob.print_name())






# num = int(input('enter num'))
# my_vector = [0, 0, 0, 0, 0, 0]
# generate_vector(num, my_vector)
