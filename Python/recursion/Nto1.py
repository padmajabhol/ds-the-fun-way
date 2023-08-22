def sol(i, n):
    if (n < i):
        return
    print(n)
    sol(i, n - 1)

sol(1, 10)
