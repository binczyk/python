import cmath as cm
import math as m
import time as t

print('\nzad 0:')
# help('statistics')

print('\nzad 1:')
a = 7 * m.sin(m.pi / 2)
b = m.cos(0) / 3
c = m.log2(18)
print(2 * ((a + b) ** (1 / 5)) - c)

print('\nzad 2:')
a = (m.factorial(30)) ** 11
print(len(str(a)))

print('\nzad 3:')
import fractions

print(fractions.gcd(m.factorial(60), 8 ** 120))
print((m.factorial(60)) % (8 ** 120))

print('\nzad 4:')
a = int('2021', 3)
b = int('10212', 3)
print(a * b)

print('\nzad 5:')
a = m.pi / 7
b = m.e ** 2
c = 3 / m.pi
print(((b * (m.tan(2.1 * a) ** c)) / (3 * (m.e ** b))) - m.cos(a + c))

print('\nzad 6:')
start = t.perf_counter()
print((cm.e ** 2j) + cm.sqrt(-5))
end = t.perf_counter()
print('duration: ', end - start)
