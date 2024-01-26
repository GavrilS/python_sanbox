def f(a, b):
    a += b
    return a


x = 1
y = 2
print('f(x, y): ', f(x, y))
print(f"x - {x}; y - {y}")
a = [1, 2]
b = [3, 4]
print('f(a, b): ', f(a, b))
print(f"a - {a}; b - {b}")
p = (10, 20)
u = (30, 40)
print('f(p, u): ', f(p, u))
print(f"p - {p}; u - {u}")
