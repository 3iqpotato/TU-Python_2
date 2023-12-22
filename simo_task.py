
import random

from numpy import average

my_list_with_nums = []
while True:
    n = int(input('Enter a number: '))
    try:
        if not 15<n<35:

            raise ValueError('Please enter a number between 15 and 35')
    except ValueError as vr:
        print(vr)
        continue

    else:
        for _ in range(n):
            my_list_with_nums.append(random.randint(30, 300))
        break

print(my_list_with_nums)

#num elements % 3 = 0
count_nums = len([number for number in my_list_with_nums if number % 3 == 0])
print(count_nums)

#find element whitch % 6 == 4
elements_with_ostatuk_4 = [number for number in my_list_with_nums if number % 6 == 4]
min_number = min(elements_with_ostatuk_4)

# tazi if проверка я слагам понеже има шанс да няма такова число и тогава ще даде грешка!!!
if min_number:
    index_of_the_element = my_list_with_nums.index(min_number)
    print(index_of_the_element)
else:
    print('No such number')

#create the new list
#проверяваме дали номера е по малък от 100 което гарантира че ще е двуцифрен и дали се дели на 2 и 3!!
new_list = [number for number in my_list_with_nums if number < 100 and number % 2 == 0 and number % 3 == 0]
print(new_list)


#AVG of the list
#брат не знам за кои списък говорят така че правя на които харесам

nums_with_odd_indexes = [number for number in my_list_with_nums if my_list_with_nums.index(number) % 2 != 0]
# print(nums_with_odd_indexes)
print(average(nums_with_odd_indexes))

#delete the min even number
even_nums = [number for number in my_list_with_nums if number % 2 == 0]
min_number = min(even_nums)
my_list_with_nums.remove(min_number)

