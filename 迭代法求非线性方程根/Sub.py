import math

f = lambda x: x * x * x - x - 1

print("本例求解x * x * x - x - 1 = 0的近似解")
a, b = map(float, input("输入区间：\n").split())
p = float(input("输入要求精度：\n"))

x = 0

while b - a >= p:
    y0 = f(a)
    x = (a + b) / 2
    y = f(x)
    if y * y0 == 0:
        break
    if y * y0 > 0:
        a = x
    else:
        b = x

print("方程的根=%.10f" % x)