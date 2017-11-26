print('zad0')

b = ['ab', ] * 6 + [2, ] * 10 + ['z', ] * 15
print(b)

print('zad1')
b[-1] = 'last'
print(b)

print('zad2')
b[len(b) // 2] = 'x'
print(b)

print('zad3')
b[1] = ('a', 2, 'zz')
print(b)

print('zad4')
del b[3:9]
print(b)

print('zad5')
del b[b.index(2)]
print(b)

print('zad6')
b[11:2:-1]
print(b[11:2:-1])
print(b[11:2:-1].index(2))
