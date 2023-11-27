import math
import turtle


def print_lines():
    print('-'*30)

#zadacha 1 lice na trapec
a, b, h = [int(x) for x in input("a, b, h = ").split(' ')]
s = ((a+b) * h) /2
round(s, 0)
print(s)
print(f'S = (a + b) * h / 2 = ({a} + {b}) * {h} / 2 = {s:.1f}')
print("S = (a + b) * h / 2 = (%d + %d) * %d / 2 = %.1f" % (a, b, h, s))
print("S = (a + b) * h / 2 = ({} + {}) * {} / 2 = {}".format(a, b, h, s))
print("S = (a + b) * h / 2 = (" + str(a) + ' + ' + str(b) + ") * " + str(h) + " / 2 = " + str(s))
print_lines()

# # zadacha 2 lice i obikolka na okruznost
r = float(input('r = '))
p = 2 * math.pi * r
s = math.pi * r**2
pi = f"{math.pi:.3f}"
print(f"S = pi * r * r = {math.pi:.3f} * {r} * {r} = {s:.3f}"
      f"\nP = 2 * pi * r = 2 * {math.pi:.3f} * {r} = {p:.3f}")
print("S = pi * r * r = %.3f * %.1f * %.1f = %.3f" \
      "\nP = 2 * pi * r = 2 * %.3f * %.1f = %.3f" % (math.pi, r, r, s, math.pi, r, p))
print("S = pi * r * r = {:.3f} * {:.1f} * {:.1f} = {:.3f}"\
      "\nP = 2 * pi * r = 2 * {:.3f} * {:.1f} = {:.3f}".format(math.pi, r, r, s, math.pi, r, p))
print("S = pi * r * r = " + pi + ' * ' + str(r) + ' + ' + str(r) + ' = '+ str(round(s, 3)) + \
      "\nP = 2 * pi * r = 2 * " + str(pi) + ' * ' +str(r) + ' = ' + str(f"{round(p, 3):.3f}"))
print_lines()

# zadacha 3 rabota
num_hours = int(input('Hours = '))
price_per_hour = float(input('Price per hour = '))
full_price = num_hours * price_per_hour
print(f"Total: {full_price:.2f}lv.")
print(f"Total:" + str(full_price) + "lv.")
print("Total: {:.2f}lv.".format(full_price))
print("Total: %.2flv." % full_price)

# drow circle
y_or_n = input("Drow Y/N: ")

if y_or_n == 'Y':
    s = turtle.TurtleScreen
    t = turtle.Turtle()
    t.color("green")
    t.circle(r * 30)
    turtle.mainloop()

else:
    print('dkahd')

