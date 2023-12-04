# l = [40, 269, 167, 299, 140]
# for i in l:
#     print(i//10z%10)
# def find(*args):
#     gcd = 0
#
#     for i in range(1, min(*args)+1):
#         if all([True if x % i == 0 else False for x in nums ]):
#             gcd = i
#
#
#     return gcd
#
#
#
# nums = [6, 12, 36, 6]
# print(find(*nums))
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        return f'{self.name}, {self.age}'
    def __str__(self):
        return self.output()

    def __repr__(self):
        return self.output()

ayugdu = Person('hoho', 4)
print(ayugdu)