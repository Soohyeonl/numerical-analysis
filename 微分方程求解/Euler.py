import matplotlib.pyplot as plt
import numpy as np
import sys

def Eulers(f, x, h, y0, n):
    y = [0] * (n + 1)
    y[0] = y0
    i = 1
    while i < n + 1:
        yp = y[i - 1] + h * f(x[i - 1], y[i - 1])
        yc = y[i - 1] + h * f(x[i], yp)
        y[i] = (yp + yc) / 2
        i += 1
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.grid()
    plt.show()
    print("  x         y")
    for i in range(n + 1):
        print("%.2f, %.10f" % (x[i], y[i]))

txt = open("./hhh", 'r')                #更换测试时注释此行
sys.stdin = txt                         #更换用例时注释此行
print("本例计算y' = y - 2 * x / y，更换函数修改lambda表达式")
f = lambda x, y: y - 2 * x / y
x0, y0 = map(float, input("初值横纵坐标：\n").split())
h = float(input("步长：\n"))
n = int(input("后移个数：\n"))
x = np.arange(x0, x0 + h * (n + 1), h)
Eulers(f, x, h, y0, n)