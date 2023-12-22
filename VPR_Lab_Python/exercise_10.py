import random


my_list_with_nums = []
while True:
    n = int(input('Enter a number: '))
    try:
        if not 20<n<30:

            raise ValueError('Please enter a number between 20 and 30')
    except ValueError as vr:
        print(vr)
        continue

    else:
        for _ in range(n):
            my_list_with_nums.append(random.randint(-100, 100))
        break

print(my_list_with_nums)
sum_odd_indexes = sum(x for x in my_list_with_nums if my_list_with_nums.index(x) % 2 != 0)
print(sum_odd_indexes)

num_elements_cratni_na_2 = [x for x in my_list_with_nums if x%10%2 == 0]
print(num_elements_cratni_na_2)
print(len(num_elements_cratni_na_2))

even_negative_nums = [x for x in my_list_with_nums if x < 0 and x % 2 ==0]
print(even_negative_nums)
start_num = 1
for num in even_negative_nums:
    start_num *= num
print(start_num)

sorted_list = sorted(my_list_with_nums, reverse=True)
print(sorted_list)

my_list_with_nums_2 = [x for x in my_list_with_nums if x > n]
print(my_list_with_nums_2)

max_num = max(my_list_with_nums_2)
min_num = min(my_list_with_nums_2)
print(max_num-min_num)

odd_nums_from_list_2 = [x for x in my_list_with_nums_2 if x % 2 != 0]
print(odd_nums_from_list_2)
print(len(odd_nums_from_list_2))

my_list_with_nums_2.remove(min_num)
print(my_list_with_nums_2)