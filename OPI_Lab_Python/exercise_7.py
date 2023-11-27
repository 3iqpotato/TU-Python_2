import random


class Student:
    def __init__(self, num_in_class, name, grade):
        self.num_in_class = num_in_class
        self.name = name
        self.grade = grade

    def print_info(self):
        print(f"{self.name} is number {self.num_in_class} with grade {self.grade}")

student_names = ['Gosho', 'Petur', 'Milen', 'Ivana', 'Misho', 'Borislav', 'Monika', 'Valeriq', 'Spasimir', 'Ivan']
students = []
for i in range(1, 11):
    g = random.randint(2, 6)
    students.append(Student(i, student_names[i-1], g))

# for student in students:
#     student.print_info()
def find_max_grade():
    max_grade = max([s.grade for s in students])
    return max_grade

while True:
    print("MENU: \n1-Принтиране на информация за участниците в списъка "
          "\n2-Извеждане на среден успех "
          "\n3-Даване на бонус 1 за всяка оценка между 2 и 3"
          "\n4-Отпечатване на максималната оценка "
          "\n5-Отпечатване на имената на участниците с максимална оценка"
          "\n6-Преброяване на учениците за поправка и изваждане на номерата им в класа"
          "\n7-Изход")

    command = int(input(f"Enter a number: "))
    if command == 1:
        print()
        for student in students:
            student.print_info()
        print()

    if command == 2:
        avg_grade = 0
        for student in students:
            avg_grade += student.grade
        print()
        print(f"Average grade is {avg_grade / len(students)}")
        print()

    if command == 3:
        for student in students:
            if 2 <= student.grade <= 3:
                student.grade += 1

    if command == 4:

        max_grade = find_max_grade()
        print()
        print(f"The maximum grede is {max_grade}")
        print()

    if command == 5:
        max_grade = find_max_grade()
        print()
        for student in students:
            if student.grade == max_grade:
                student.print_info()
        print()

    if command == 6:
        bad_students = [student for student in students if student.grade < 3]
        print()
        print(f"Студентите за поправка са {len(bad_students)} и номерата им са {', '.join(str(x.num_in_class) for x in bad_students)}")
        print()

    if command == 7:
        print('Exit')
        break