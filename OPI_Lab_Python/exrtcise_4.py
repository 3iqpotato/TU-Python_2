# #task 1
# number = input("Enter a number: ")
# print(tuple(int(x) for x in number))
# print(tuple(int(x) for x in reversed(number)))
#
# #task 2
# numbers = []
# while True:
#     num = input("Enter a number: ")
#     if num == "stop":
#         break
#     numbers.append(int(num))
#     if len(numbers) > 1:
#         sum_nums = numbers[-2] + numbers[-1]
#         numbers.insert(-1, sum_nums)
# 
# print(numbers)

#task 3
# text = input("Enter a text: ")fff2
# keys = set(text)
# dict_letters = {}
# for k in keys:
#     dict_letters[k] = text.count(k)
# print(dict_letters)

#task 4
# number = int(input("Enter a number: "))
# numbers = [x for x in range(1, number+1)]
# dict_nums = {}
# for num in numbers:
#     dict_nums[num] = numbers[-num]
#
# print(dict_nums)
