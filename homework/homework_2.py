import cmath
from decimal import Decimal as D
from decimal import getcontext
from fractions import Fraction as F

print("\nzad1")
print(round(D('1.4') * D('1.025'), 2))

print("\nzad2")
print(D('10.5') % D('0.2'))

print("\nzad3")
getcontext().prec = 500
print(D(1).exp())

print("\nzad4")

print((2 + F(1, 2)) * F(3, 5) + (2 + F(1, 10)) * (9 + F(2, 17)) - (7 + F(81, 100)))

print("\nzad5")
a = 1 + F(1, 10)
b = F(-1, 2)
c = 3 + F(2, 21)
print(c * (a + b) + a * b - 2 * c + F(a, c))

print("\nzad6")
print(F(D(1).exp()).limit_denominator(19))

print("\nzad7")
a = F(int('232', 4), int('211', 3))
b = F(int('5463', 8), int('325', 6))
print(a - b)
