import math


def trapezoid(f, a, b, p):
    h = b - a
    T1 = h * (f(a) + f(b)) / 2
    s = 0
    x = a + h / 2
    while x < b:
        s += f(x)
        x += h
    T2 = T1 / 2 + h * s / 2
    while abs(T2 - T1) >= p:
        h /= 2
        T1 =T2
        s = 0
        x = a + h / 2
        while x < b:
            s += f(x)
            x += h
        T2 = T1 / 2 + h * s / 2

    return T2


y = lambda x: math.sin(x)
print("此例求解的是y = sin(x)的积分，其他函数请修改lambda表达式")
a, b = map(float, input("输入积分区间：").split())
p = float(input("精度要求（如0.001）："))
print(trapezoid(y, a, b, p))
