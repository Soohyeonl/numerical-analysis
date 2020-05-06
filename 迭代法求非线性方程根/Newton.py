import math

f = lambda x: x * math.exp(x) - 1
df = lambda x: (x + 1) * math.exp(x)

print("本例求解x * e ^ x - 1 = 0的近似解")
x0, p = map(float, input("输入初值和精度：").split())
N = int(input("迭代次数："))

flag = False
k = 1
while k < N:
    if df(x0) == 0:
        flag = True
        break
    x1 = x0 - f(x0) / df(x0)
    if abs(x0 - x1) < p:
        print("方程的近似根=%.10f" % x1)
        break
    else:
        k += 1
        x0 = x1

if flag == True:
    print("迭代过程中导数值为0，失败")
elif k == N:
    print("迭代方法失败")