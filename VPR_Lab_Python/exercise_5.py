# #example_1
# def greet():
#     print('Hello!')
#
# greet()
# #example_2
# def greet_person(name):
#     print(f'Hello {name}!')
#
#
# greet_person('Gosho')
# #example_3
# def add(num1, num2):
#     return num1 + num2
#
# number1 = int(input('Enter a number '))
# number2 = int(input('Enter a number '))
# result = add(number1, number2)
# print(result)
# print(f'{number1} + {number2} = {result}')
# #example_4
# def sum_array_numbers(numbers):
#     sum_nums = 0
#     for n in numbers:
#         sum_nums += n
#     return sum_nums
#
# nums = [3, 4, 5, 6, 7, 8]
# print(sum_array_numbers(nums))
# #example_5
# def dbe_array_elements(numbers):
#     for i in range(len(numbers)):
#         numbers[i] *= 2
#     return numbers
#
# nums = [3, 4, 5, 6]
# print(dbe_array_elements(nums))
# #example_6
# def sum_numbers(*numbers):
#
#     sum_nums = 0
#     for n in numbers:
#         sum_nums += n
#
#     return sum_nums
#
# print(sum_numbers(3, 4, 5, 6, 7, 8))
#
# #example_7
# function_1 = lambda x, y: x + y
# function_2 = lambda x,y: x*y
#
# def do_operations(n1, n2, function):
#     return function(n1,n2)
#
#
# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter a number: '))
#
# res_1 = do_operations(num1, num2, function_1)
# res_2 = do_operations(num1, num2, function_2)
# print(f"Lambda result: {res_1}")
# print(f"Lambda result: {res_2}")
