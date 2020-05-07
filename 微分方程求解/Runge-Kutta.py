import sys
import numpy as np
import matplotlib.pyplot as plt


def RungeKutta(f, x, h, y0, n):
    y = [0] * (n + 1)
    y[0] = y0
    i = 1
    while i < n + 1:
        K1 = f(x[i - 1], y[i - 1])
        K2 = f(x[i - 1] + h / 2, y[i - 1] + h * K1 / 2)
        K3 = f(x[i - 1] + h / 2, y[i - 1] + h * K2 / 2)
        K4 = f(x[i], y[i - 1] + h * K3)
        y[i] = y[i - 1] + h * (K1 + 2 * K2 + 2 * K3 + K4) / 6
        i += 1
    print("  x         y")
    for i in range(n + 1):
        print("%.2f, %.10f" % (x[i], y[i]))
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.grid()
    plt.show()

print("本例计算y' = y - 2 * x / y，更换函数修改lambda表达式")
f = lambda x, y: y - 2 * x / y
x0, y0 = map(float, input("初值横纵坐标：\n").split())
h = float(input("步长：\n"))
n = int(input("后移个数：\n"))
x = np.arange(x0, x0 + h * (n + 1), h)
RungeKutta(f, x, h, y0, n)
