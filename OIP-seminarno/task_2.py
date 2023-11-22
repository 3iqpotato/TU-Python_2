# import random
# import string
#
# my_string = 'петър плет плете, през три плета преплита'
#
#
# my_string_list = []
# for i in my_string:
#     if i in [',', ' ', 'и']:
#         continue
#
#     my_string_list.append(i)
#
# my_string_list[0] = my_string_list[0].upper()
# print(''.join(my_string_list))
# new_string = ''.join(my_string_list)
#
# #броене на символите и променяне
# print(new_string.count('пл'))
# new_string = new_string.replace('пл', 'ПЛ')
# print(new_string)
#
# #разделяне с точка и запетая
# print(';'.join(my_string_list))
# new_string = ';'.join(my_string_list)
# #4
# new_list = []
# for idx in range(0, len(new_string)):
#
#     if new_string[idx] == ';' and new_string[idx+1] in ['п', 'П']:
#         new_list.append(' ')
#     else:
#         new_list.append(new_string[idx])
#
# new_string=''.join(new_list)
# print(new_string)
# #5
# print(new_string.replace(';', ''))
# #6
# if 'ъ' in new_string or 'v' in new_string:
#     print('Yes')
# else:
#     print('No')
#
# #задача 2
# my_nums = [12, 3, 456, 78]
#
# first_num = ''.join(str(x) for x in my_nums)
# second_num_list = list(first_num)
# second_num_list.insert(2, '.')
# second_num_list.insert(4, '*')
# second_num_list.insert(6, '.')
# second_num_list.insert(9, '/')
# second_num_list.insert(11, '.')
# second_num = ''.join(second_num_list)
# third_num = '+'.join(str(x) for x in my_nums)
# print()
# print(eval(first_num))
# print(f"{eval(second_num):.2f}")
# print(eval(third_num))
# print()
# #задача 3
# first_names = ['Алекс', 'Евгени', 'Цвета', 'Петя', 'Дарина']
# second_names = ['Алекс', 'Мирослав', 'Цвета', 'Радка', 'Дарина', 'Анна', 'Биляна']
# third_names = ['Стоян', 'Радка', 'Евгини', 'Дарина', 'Анна', 'Камен', 'Петя', 'Цвета']
# all_names = ['Анна', 'Алекс', 'Биляна', 'Евгени', 'Дарина', 'Камен', 'Катя', 'Мирослав', 'Петя', 'Радка', 'Стоян', 'Цвета']
#
# student_in_all_lectures = []
# student_in_first_lecture = []
# students_atleast_at_one_lecture = []
# student_not_on_lecture = []
# for student in all_names:
#     if student in first_names and student in second_names and student in third_names:
#         student_in_all_lectures.append(student)
#
#     if student in first_names and student not in second_names:
#         student_in_first_lecture.append(student)
#
#     if student in first_names or student in second_names or student in third_names:
#         students_atleast_at_one_lecture.append(student)
#     else:
#         student_not_on_lecture.append(student)
#
# print(f'На всички занятия са били: {", ".join(student_in_all_lectures)}')
# print(f"Само на първата лекция са били {', '.join(student_in_first_lecture)}")
# print(f"Студентите които са били поне в едно занятие са: {', '.join(students_atleast_at_one_lecture)}")
# print(f"Студенти които не са били в лекции: {', '.join(student_not_on_lecture)}")
# print()
#
# #задача 4
# dict_student = {}
# for student in all_names:
#     dict_student[student] = 0
#     if student in student_in_all_lectures:
#         dict_student[student] += 3
#
#     elif student in first_names:
#         dict_student[student] += 1
#
#     elif student in second_names:
#         dict_student[student] += 1
#
#     elif student in third_names:
#         dict_student[student] += 1
#
# for student, times in dict_student.items():
#     print(f'Студента {student} е бил {times} на лекции')
#
# print()
#
# num = int(input('Въведете число:'))
#
# my_string = ''
# for i in range(num):
#     letter = random.choice(string.ascii_uppercase)
#     my_string += letter
#
# print(tuple(my_string))
# print(f'Множеството от елементи е {set(my_string)}')
# print(f'Списък е слементите е {list(set(my_string))}')
# list_letters_and_counts = []
# list_counts = []
#
# for letter in my_string:
#     list_counts.append(my_string.count(letter))
#     print(list_counts)
#     list_letters_and_counts.append((letter, my_string.count(letter)))
#
# print(list_letters_and_counts)
# dict_letters_and_count = {}
# for t in list_letters_and_counts:
#     dict_letters_and_count[t[0]] = t[1]
#
# print(dict_letters_and_count)
# print()
#
#
# #задача 7
# list_nums = []
# for i in range(1, 50):
#     if i % 3 == 0:
#         list_nums.append(i)
#
# print(list_nums)
# for i in list_nums:
#     if i % 4 == 0:
#         list_nums.remove(i)
#
# print(list_nums)
#
# new_list_nums = []
# for i in range(1, 50):
#     if i % 5 == 0:
#         new_list_nums.append(i)
#
# print(new_list_nums)
#
# i = 0
# for idx in range(1, len(list_nums)):
#     if idx % 2 == 0:
#         i += 1
#         list_nums.insert(idx, (new_list_nums[i]))
#
# print(list_nums)
# print(sorted(list_nums, reverse=True))
# for el in list_nums:
#     if list_nums.count(el) > 1:
#         list_nums.remove(el)
#
# print(list_nums)
# print()
#
#
#
#
#
#
#
#
# #задача 10
# nums = [0, 1, 2, 3, 4, 5]
# nums_to_add = []
# for idx in range(len(nums)-1):
#     nums_to_add.append((nums[idx] + nums[idx+1]) / 2)
#
# print(nums)
# print(nums_to_add)
# len_nums = len(nums) -1
# idx = 1
# for i in range(len_nums):
#     nums.insert(idx, nums_to_add[i])
#     idx += 2
# print(nums)
how_to_be = ['r', 'b', 'r', 'b', 'r', 'b', 'r', 'b']
# how_to_be = ['r', 'r', 'r', 'r', 'b', 'b', 'b', 'b']
# cards = ['r', 'b', 'r', 'b', 'r', 'b', 'r', 'b']

for i in range(8):

    new_def_cards = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
    new_def_cards[i] = 'b'
    for j in range(i, 8):
        second_def_cards = new_def_cards.copy()
        second_def_cards[j] = 'b'

        for k in range(j, 8):
            third_def_cards = second_def_cards.copy()
            third_def_cards[k] = 'b'

            for  m in range(k, 8):
                def_cards = third_def_cards.copy()
                def_cards[m] = 'b'
                how_are_cards_now = def_cards.copy()
                open_cards = []
                n = 0
                while def_cards:
                    if n > len(def_cards):
                        n = 0
                    open_cards.append(def_cards[n])
                    def_cards.pop(n)
                    if len(def_cards) > 0:
                        def_cards.append(def_cards.pop(n))

                # print(open_cards)
                if open_cards == how_to_be:
                    print(how_are_cards_now)
                    print(open_cards)

#
#
