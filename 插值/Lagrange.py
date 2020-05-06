def lagrange(x, y, n, x0):
    k = 0
    res = 0
    while k < n:
        t = 1.0
        i = 0
        while i < n:
            if i == k:
                i += 1
                continue
            t *= ((x0 - x[i]) / (x[k] - x[i]))
            i += 1
        res += t * y[k]
        k += 1
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
print("x0点的Lagrange插值近似值=%f" % (lagrange(x, y, n, x0)))