import math

from VPR_Lab_Python.exercise_8_part_2 import check_number_2

# with open('test_file', 'r') as f:
#     print(f.read())
#     print(f.name)

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = a / b
# #     print(f"c=a/b => {a}/{b}={c}")
# except ZeroDivisionError:
#     print("cant divide by zero")
# except :
#     print(f'Something went wrong')
#
# try:
#     grades = [6, 5, 6, 2, 4, 6, 3, 5, 3, 2, 6]
#     student = int(input("student N: "))
#     print(f"Student with N {student} achieved {grades[student - 1]}")
#
# except IndexError as message:
#
#     print(f'{message}')
#     print(f'{type(message)}')
#     print(f'{message.__class__}')
#     print(f'{message.__class__.__name__}')
#
#     print(f'Index {student} is out of range')
#
# except ValueError:
#
#     print(f'Input must be a number')

# finally:
#     print(f'Done')
#
#
# print(f'Goodbye')



# num = input('Enter a number: ')
#
# try:
#     num = int(num)
#
#     if num < 0:
#         raise Exception
#
#     else:
#         print(math.sqrt(num))
#
# except Exception:
#     print('Invalid Number')
#
# finally:
#     print('Good Bye')

def check_number(number):

    if number < 0:
        raise Exception('The number must be positive')

    else:
        return math.sqrt(number)


try:
    number = int(input('Enter a number: '))
    my_num = check_number(number)
    print(my_num)

except ValueError as ve:
    print(ve.args[0])

except Exception as ex:
    print(f"{ex.args[0]}")

# import random
#
# grade = random.randint(2, 6)
# print(grade)

#import from other file

try:
    number = int(input('Enter a number: '))
    my_num = check_number_2(number)
    print(my_num)

except ValueError as ve:
    print(ve.args[0])

except Exception as ex:
    print(f"{ex.args[0]}")