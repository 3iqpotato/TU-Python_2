#task_1
def find_square_area(a):
    return a * a

def find_rectangle_area(a, b):
    return a * b

def find_triangle_area(a, b):
    return (a * b) / 2

# figure_type = input(f"Enter figure type: ")
# if figure_type == 'square':
#     a = int(input(f"a = "))
#     print(f"Square area = {find_square_area(a)}")
# elif figure_type == 'rectangle':
#     a = int(input(f"a = "))
#     b = int(input(f"b = "))
#     print(f"Rectangle area = {find_rectangle_area(a, b)}")
# elif figure_type == 'triangle':
#     a = int(input(f"a = "))
#     b = int(input(f"b = "))
#     print(f"Rectangle area = {find_triangle_area(a, b)}")

# # task 2
# number = int(input('Enter a number: '))
def is_palindrome(num):
    rev_num = int(str(num)[::-1])
    if rev_num == num:
        return 1
    return 0


# print(is_palindrome(number))
# #
# # task 3
def subtraction(a, b):
    return a-b

def gathering(a, b):
    return a+b

def multiplication(a, b):
    return a*b

def division(a= 9, b= 9):
    return a/b



# operation = input('Enter operation: ')
# num1 = float(input('Enter first number: '))
# num2 = float(input('Enter second number: '))
# #
# if operation == '+':
#     print(gathering(num1, num2))
# elif operation == "-":
#     print(subtraction(num1, num2))
# elif operation == '*':
#     print(multiplication(num1, num2))
# elif operation == "/":
#     print(division())
#
# # task 4
# def some_func(number, *nums):
#     nums = list(nums)
#     for idx in range(len(nums)):
#         if nums[idx] > number:
#             nums[idx] = 0
#     return nums
#
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_num = int(input('Enter a number: '))
# print(numbers)
# print(some_func(my_num, *numbers))
#
