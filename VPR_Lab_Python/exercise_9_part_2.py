import json

class Student:
    def __init__(self, number, name, grade):
        self.number = number
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'number: {self.number} name: {self.name} grade: {self.grade} '

    def __repr__(self):
        return self.__str__()

#simo ako chetesh tova tozi klas otdolu e prosto za da raboti zashtoto inache ne stava
class StudentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return obj.__dict__
        return super().default(obj)

names = ['Spasimir', 'Georgi', ' Nadezda', 'Martin']
grades = [4, 5, 6, 2]
students = []
for idx in range(len(names)):
    students.append(Student(idx+1, names[idx], grades[idx]))
#
dagu = json.dumps(students, cls=StudentEncoder)

with open('students_2.json' , 'w') as f:
    f.write(dagu)

with open('students_2.json' , 'r') as f:
    print(f.readlines())


with open('students_3.bin', 'w') as f:
    f.write(json.dumps(json.dumps(students, cls=StudentEncoder)))

with open('students_3.bin', 'r') as f:
    print(f.readlines())

#Not working!!!
# import pickle
#
# bin_student_pickle = pickle.dumps(students)
# print(bin_student_pickle)
# with open("students.bin", "w") as f4:
#     f4.write(str(bin_student_pickle))
#
# with open("students2.bin","w") as f5:
#     f5.write(json.dumps(students))
#
# with open("students2.bin","r") as f6:
#     print(type(pickle.load(f6)))
#     for i in pickle.load(f6):
#         print(i)