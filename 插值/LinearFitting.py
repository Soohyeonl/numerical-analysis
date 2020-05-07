import matplotlib.pyplot as plt
import numpy as np

def linearFitting(x, y, n):
    a, b = 0, 0
    xy_n = 0
    x_n = 0
    y_n = 0
    x2_n = 0
    for i in range(n):
        xy_n += x[i] * y[i]
        x_n += x[i]
        y_n += y[i]
        x2_n += x[i] * x[i]
    b = ((n * xy_n - x_n * y_n) / (n * x2_n - x_n * x_n))
    a = ((y_n * x2_n - x_n * xy_n) / (n * x2_n - x_n * x_n))
    return a, b

n = int(input("输入插值点个数："))
min, max = map(int, input("区间最小值和最大值：").split())
print("输入各点的自变量和函数值：")
i = 0
x = []
y = []

while i < n:
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    i += 1

a, b = linearFitting(x, y, n)
x_ = np.arange(min, max, 0.1)
y_ = a + b * x_
plt.title("p=" + str(a) + "+" + str(b) + "x", fontsize=24)
plt.plot(x_, y_)
plt.scatter(x, y)
plt.show()
print("拟合曲线为：p = %.4f + %.4fx" % (a, b))