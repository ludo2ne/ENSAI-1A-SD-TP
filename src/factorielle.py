def fac_for(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def fac_while(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


def fac_rec(n):
    if n == 0 or n == 1:
        return 1
    return fac_rec(n - 1) * n


print(fac_rec(5))
