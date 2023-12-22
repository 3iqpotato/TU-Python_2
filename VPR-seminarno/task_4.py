import math


#task 1
class Vector:
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        n = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        print(f'n = {n}')
        return n

vector1 = Vector('vectorA', 3, 4 ,5)
vector2 = Vector('vectorB', 7, 8, 9)
a = vector1.norm()
b = vector2.norm()

#task2
class Scalar(Vector):

    @staticmethod
    def scalarproduct(v1, v2):
        c = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
        print(f'scalar = {c}')
        return c

    @staticmethod
    def cosalpha(c, len_a, len_b):
        calpha = c / (len_a * len_b)
        alpha = math.acos(calpha) * (180/math.pi)  # to be continue
        print(f'cosalpha = {calpha}')
        print(f'alpha = {alpha}')
        return alpha
    @staticmethod
    def proverka(deg, a, b):
        sp = abs(a)*abs(b)*math.cos(deg*math.pi/180)
        print(f'proverka = {sp}')
        return sp

#test
vectorA = Scalar('VectorA', 3, 4, 5)
vectorB = Scalar('VectorB', 1, 0, 2)
len_A = vectorA.norm()
len_B = vectorB.norm()
print(f'VecrotA - {len_A}')
print(f'VecrotB - {len_B}')
scalarproduct_of_vectors = vectorA.scalarproduct(vectorB, vectorA)
# print(scalarproduct_of_vectors)
alpha = vectorA.cosalpha(scalarproduct_of_vectors, len_A, len_B)
proverkata = vectorA.proverka(alpha, len_A, len_B)

#task 4
def somefunction(a, b, c):
    try:
        d = b**2 - 4*a*c
        print(f'D = {d}')
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        return x1, x2
    except ValueError:
        return somefunction(a, b+1, c)
    except ZeroDivisionError:
        return -c/b



x1, x2 = somefunction(1, 2, 1)
print(x1, x2)

x1, x2 = somefunction(1, 4, 1)
print(x1, x2)

x1, x2 = somefunction(1, 1, 1)
print(x1, x2)

try:
    x1, x2 = somefunction(0, 2, 1)
    print(x1, x2)

except TypeError:
    x1 = somefunction(0, 2 ,1)
    print(x1)

try:
    x1, x2 = somefunction(2, 1)

except TypeError:
    x1 = somefunction(0, 2, 1)
    print(x1)

#task 8
class MyClass:
    def __init__(self, text, number):

        if type(number) == type('str') and type(text) == type('str'):
            self.text = text + number
        elif type(number) == type(1) and type(text) == type(1):
            self.number = text + number
        else:
            self.text = text
            self.number = number

ob1 = MyClass(90, 4)
print(ob1.number)
ob2 = MyClass('doahiguoida', 'dtagyuiojda')
print(ob2.text)
ob3 = MyClass('daui', 9)
print(ob3.__dict__)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Boss(Person):
#     pass
#
# loli = Boss('piko', 123)
# print(loli.name)