# people = int(input('How many people: '))
# people_count = 0
#
# while people_count < people:
#     age = int(input(f'Person {people_count + 1} enter age: '))
#     while not (18 < age < 120):
#         print('Error: Invalid age must be between 18 and 120!!!')
#         age = int(input(f'Person {people_count + 1} enter age: '))
#
#     people_count += 1
#
# print(f'Success registered {people_count} people')
#

# count_nums = int(input('How many nums: '))
# sum_nums = 0
# for _ in range(count_nums):
#
#     num = int(input('Enter number: '))
#     sum_nums += num
#
# print(f'The sum of the numbers is {sum_nums}')

#drow full rectangle
# rows = int(input('Enter number of rows: '))
# for _ in range(rows):
#     print('* ' * 5)

#drow empty rectangle
# rows = int(input('Enter number of rows: '))
# print('* ' * 5)
# for _ in range(1, rows-1):
#
#     print("*" + ' '*7 + '*')
# print('* ' * 5)

#draw triangle
# rows = int(input('Enter number of rows:'))
# for i in range(1, rows+1):
#     print('*' * i + ' ' * (((rows - i) * 2) + 1) + '*' * i)
# for i in range(rows-1, 0, -1):
#     print('*' * i + ' ' * (((rows - i) * 2) + 1) + '*' * i)
#
# rows = int(input('Enter number of rows:'))
# for i in range(1, rows+1):
#     print('* ' * i)