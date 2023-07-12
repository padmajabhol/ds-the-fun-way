def linearSearch(A, target):
    i = 0
    while i < len(A):
        if A[i] == target:
            return i
        i = i + 1
    return -1

print(linearSearch([3,4,1,7], 4))

