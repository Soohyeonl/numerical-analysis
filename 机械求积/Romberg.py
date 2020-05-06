import math


def Romberg(f, a, b, p):
    h = b - a
    T1 = h * (f(a) + f(b)) / 2
    print("T1 = %f" % T1)
    k = 1
    S1 = 0
    C1 = 0
    R1 = 0
    R2 = 0
    while True:
        s = 0
        x = a + h / 2
        while x < b:
            s += f(x)
            x += h
        T2 = T1 / 2 + h * s / 2
        print("T%d = %f" % (math.pow(2, k), T2))
        S2 = T2 + (T2 - T1) / 3
        print("S%d = %f" % (math.pow(2, k), S2))
        if k == 1:
            k += 1
            h /= 2
            T1 = T2
            S1 = S2
            continue
        C2 = S2 + (S2 - S1) / 15
        print('C%d = %f' % (math.pow(2, k), C2))
        if k == 2:
            C1 = C2
            k += 1
            h /= 2
            T1 = T2
            S1 = S2
            continue
        R2 = C2 + (C2 - C1) / 63
        print('R%d = %f' % (math.pow(2, k), R2))
        if k == 3:
            R1 = R2
            C1 = C2
            k += 1
            h /= 2
            T1 = T2
            S1 = S2
            continue
        if abs(R2 - R1) < p:
            break
        R1 = R2
        C1 = C2
        k += 1
        h /= 2
        T1 = T2
        S1 = S2
        continue
    return R2


y = lambda x: math.sin(x)
print("此例求解的是y = sin(x)的积分，其他函数请修改lambda表达式")
a, b = map(float, input("输入积分区间：").split())
p = float(input("精度要求（如0.001）："))
print(Romberg(y, a, b, p))
