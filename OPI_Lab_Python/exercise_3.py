my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[2:-5])
print(my_list[-4:-2])
print(my_list[-6:-4]) # винаги първия трябва да е по малкъ от 2рия

#увеличаване на стоиностите с 1
for i in range(len(my_list)):
    my_list[i] += 1

print(my_list)
