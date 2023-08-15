def reversed(nums):
    reverse = 0
    while nums != 0:
        digit = nums % 10
        reverse = reverse * 10 + digit
        nums = nums // 10
    return reverse

print(reversed(1234))
        
