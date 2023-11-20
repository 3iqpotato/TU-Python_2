# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
#
# sum_nums = 0
# for i in range(a, b + 1):
#     sum_nums += i
#
# print(sum_nums)
# a, b = [int(x) for x in input('Enter first and second number: ').split()]
# sum_nums = 0
# while a < b+1:
#     sum_nums += a
#     a += 1
#
# print(sum_nums)
# #task 2
# while True:
#     a = int(input('Enter first number: '))
#     b = int(input('Enter second number: '))
#
#     sum_nums = 0
#     for i in range(a, b + 1):
#         sum_nums += i
#
#     print(sum_nums)
#
#     print('Ще въвеждате ли още числа Y \\ N')
#     choice = input()
#     if choice.lower() == 'n':
#         print('Good bye')
#         break
# task 3
# num = int(input('Enter number: '))
# fac_num = 0
# while num > 0:
#     fac_num += num
#     num -= 1
#
# print(f'n! = {fac_num}')
import math
import random
import statistics

from numpy import average
#
# # num = int(input('Enter number: '))
# # fac_num = 0
# # for i in range(num+1):
# #     fac_num += i
# #
# # print(f'n! = {fac_num}')
#
# #task 4
# x = int(input('Enter number X: '))
# n = int(input('Enter number N: '))
#
# sum_nums = 0
# for i in range(n+1):
#     sum_nums += x**i
#
# print(sum_nums)
# x = int(input('Enter number X: '))
# n = int(input('Enter number N: '))
#
# sum_nums = 0
# a = 1
#
# while i < n+1:
#     sum_nums += 1
#     a *= x
#
# print(sum_nums)
#
# # task 5
# times = [41.0, 43.4, 48.8, 49.2, 50.1, 44.6, 47.3, 46.8, 43.9, 46.4]
# avg_time = average(times)
# print(f'AVG time = {avg_time}')
#
# error_times = []
# square_error_times = []
# n = len(times)
# for time in times:
#     error_time = time-avg_time
#     square_error_time= error_time ** 2
#
#     print(error_time, square_error_time)
#
#     error_times.append(error_time)
#     square_error_times.append(square_error_time)
#
# sum_error_times = sum(square_error_times)
# print(f'{sum_error_times}')
#
#
# once_square_mistake = math.sqrt(sum_error_times / n*n-1)
# print(once_square_mistake)
#
# absolute_error = avg_time + average(square_error_times)
# print(f"{absolute_error} 68% вероятност")
# #
# print(statistics.stdev(times))
#
#
#task 6
# for i in range(10):
#     n = random.gauss(2.023, 0.014)
#     print(f"{n:.3f}")
#
# for i in range(10):
#     n = random.uniform(10, 16)
#     print("%d" % n)
#
# for i in range(10):
#     n = random.randint(10, 16)
#     print(f'{n:.2f}')
#
# for i in range(10):
#     n = random.random()
# #     print(f'{n:.2f}')
# nums = []
# for i in range(11):
#     n = random.uniform(1, 6)
#     nums.append(n)
#     print(f'The number is %d' % (n,))
#
# n = float('-inf')
# for i in range(len(nums)):
#     print(nums[i])
#     if nums[i] > n:
#         n = nums[i]
#
# print(f'Max num is {n}')


str_num = input()
num = 0
str_num = str_num[::-1]
for i in range(len(str_num)):
    if str_num[i] == 'A':
        n = 10 * 16 ** i

    elif str_num[i] == 'B':
        n = 11 * 16 ** i

    elif str_num[i] == 'C':
        n = 12 * 16 ** i

    else:
        n = int(str_num[i]) * 16 ** i
    num += n

print(num)







# list_nums = []
# for i in range(10):
#     number = random.gauss(1.851, 0.008)
#     print(f'{number:.3f}')
#     list_nums.append(number)
#
# for i in range(len(list_nums)):
#     print(list_nums[i])
#
# print(f'The sum is {sum(list_nums)}')
# print(f'Avg sum is {average(list_nums)}')