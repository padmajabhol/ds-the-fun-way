def sol(str1):
    list1 = []
    for i in str1.lower():
        if i.isalnum():
            list1.append(i)
    first = 0
    last = len(list1) - 1
    while first < last:
        if list1[first] != list1[last]:
            return False
        else:
            first += 1
            last -= 1
    return True

print(sol("kata"))

