def palindrome(s):
    list1 = []
    for i in s.lower():
        if i.isalnum():
            list1.append(i)
    return list1

print(palindrome("A man, a plan, a canal: Panama"))
