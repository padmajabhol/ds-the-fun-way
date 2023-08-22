def sol(i, n):
    if i > n:
        return
    print(i)
    sol(i+1,n)

sol(1, 10)
