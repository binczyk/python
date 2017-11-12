import math as m
import cmath as cm
import time as t

print('zad 0:')
# help('statistics')

print('zad 1:')
a = 7 * m.sin(m.pi / 2)
b = m.cos(0) / 3
c = m.log2(18)
print(2 * ((a + b) ** (1 / 5)) + c)

print('zad 1:')
a = (m.factorial(30)) ** 11
print(len(str(a)))

print('zad 2:')
print((m.factorial(60)) % (8 ** 120))

print('zad 3:')
a = int('2021', 3)
b = int('10212', 3)
print(a + b)

print('zad 4:')
a = m.pi / 7
b = m.e ** 2
c = 3 / m.pi
print((b * m.tan(2.1 * a) ** c) - m.cos(a - c))

print('zad 5:')

start = t.perf_counter()
print((cm.e ** 2j) + (-5 ** (1 / 2)))
end = t.perf_counter()
print('duration: ', end - start)
