def Newton(x, y, n, x0):
    res = 0
    f = [[0] * n for i in range(n)]
    for i in range(n):
        f[i][0] = y[i]
    k = 1
    while k < n:
        i = k
        while i < n:
            f[i][k] = ((f[i][k - 1] - f[i - 1][k - 1]) / (x[i] - x[i - k]))
            i += 1
        k += 1
    i = 0
    while i < n:
        k = 0
        t = f[i][i]
        while k < i:
            t *= (x0 - x[k])
            k +=1
        res += t
        i += 1
    return res

n = int(input("输入插值点个数："))
print("输入各点的自变量和函数值：")
i = 0
x = []
y = []

while i < n:
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    i += 1

x0 = int(input("输入所求点x0："))
print("x0点的Newton插值近似值=%f" % (Newton(x, y, n, x0)))