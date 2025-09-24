def fibo(n):
    if n == 1:
        return [0]

    f0, f1 = 0, 1
    liste = [f0, f1]

    for i in range(2, n):
        f0, f1 = f1, f0 + f1
        liste.append(f1)
    return liste


print(fibo(10))
