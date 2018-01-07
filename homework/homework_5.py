from sympy import *

init_printing()

x, y, a, b, c, d, e, n = symbols('x,y,a,b,c,d,e,n')

print('zad1')
print(simplify((x ** 2 + x) / ((x * sin(y) ** 2) + (x ** cos(y) ** 2))))

print('zad2')
print(limit((1 / x) * (log(exp(1) ** x + 1)), x, -oo))

print('zad3')
print(solveset(x ** 2 + 2 > x ** 3, x, S.Reals) & solveset(sqrt(x + 2) > x, x, S.Reals))

print('zad4')
print(solveset(a * x ** 3 + b * x ** 2 + c * x + d, x))

print('zad5')
print(diff(sin(x + y) * cos(x * y), x, y).evalf(subs={x: -1, y: 2}).evalf(30))

print('zad6')
print(plot(3 * x ** 2, diff(x, x), (x, 0, 5)))

print('zad7')
print(plot(limit((1 + 1 / n) ** (n * x), n, oo), x, (x, -1, 1)))

print('zad8')
print(integrate(exp(1) ** (-x ** 2), (x, -oo, oo)).evalf(50))

print('zad9')
print(plot(integrate(exp(1) ** (-x ** 2)), x, (x, -4, 4)))

print('zad10')
ax, ay, bx, by, cx, cy = symbols('ax,ay,bx,by,cx,cy')
area = abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by) / 2)
print(area.evalf(subs={ax: 0, ay: 0, bx: 2, by: 2, cx: 4, cy: 0}))
