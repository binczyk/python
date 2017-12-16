print('zad0')

import math
import random
import statistics as s
import time
from fractions import Fraction as F
from functools import reduce

doubleList = [random.uniform(0, 9) for _ in range(40)]
print(doubleList)

print('zad1')

print('the mean: ', s.mean(doubleList))
# print('the mode: ', s.mode(list))
print('the median: ', s.median(doubleList))

print('zad2')
print(any(2 <= (x ** 2) < 5 for x in doubleList))

print('zad3')

print(reduce(lambda a, b: a * b, (x * 2 ** (5 * x) for x in doubleList))
      - min(v - 4 + (3 * (math.sin(v) ** 2)) if v > 5
            else v ** 2 + (5 * math.cos(v) ** 3) for v in doubleList))

print('zad4')
print(max(list(x - 8 for x in doubleList), key=abs))

print('zad5')
print(max(list(i * val - i for itr, val in enumerate(doubleList) for i in range(40))))

print('zad6')
bList = (2, 3, 8, 9)
print(sum(a / b for a in doubleList for b in bList))

print('zad8')

start = time.perf_counter()
sum(1 / d for d in range(1, 10001))
end = time.perf_counter()
print('sum(1/d) time: ', end - start)

start = time.perf_counter()
math.fsum(1 / d for d in range(1, 10001))
end = time.perf_counter()
print('fsm(1/d) time: ', end - start)

start = time.perf_counter()
sum(F(1, d) for d in range(1, 10001))
end = time.perf_counter()
print('sum(F(1,d) time: ', end - start)
