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

names = ['Spasimir', 'Georgi', ' Nadezda', 'Martin']
grades = [4, 5, 6, 2]
students = []
for idx in range(len(names)):
    students.append(Student(idx+1, names[idx], grades[idx]))


with open('students.txt', 'wt') as f:
    for student in students:
        f.write(f'{student.number}, {student.name}, {student.grade}'+ '\n')

file1 = open('students.txt', 'a')
file1.write('5, Kaloyan, 3')
file1.close()

students_info = []
with open('students.txt', 'r') as f:
    print(f.readlines())
    f.seek(0)
    students_info.extend(f.readlines())

students_2 = []
for student_info in students_info:
    info = student_info.split(', ')
    students_2.append(Student(info[0], info[1], info[2][:1]))

for student in students_2:
    print(student)
