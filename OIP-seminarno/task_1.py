a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

sum_nums = 0
for i in range(a, b + 1):
    sum_nums += i

print(sum_nums)
a, b = [int(x) for x in input('Enter first and second number: ').split()]
sum_nums = 0
while a < b+1:
    sum_nums += a
    a += 1

print(sum_nums)
