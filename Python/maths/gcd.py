def gcd(num1, num2):
    ans = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            ans = i

    return i

print(gcd(4, 8))

