def reverse(num1):
    reversenum = 0
    num2 = num1
    while num1 > 0:
        digit = num1 % 10
        reversenum = reversenum * 10 + digit
        num1 = num1 // 10
    if num2 == reversenum:
        return True
    return False

print(reverse(123))
