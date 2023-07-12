def insertionSort(A):
    n = len(A)
    i = 1
    while i < n:
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = current
        i = i + 1

    return [0]

print(insertionSort([5,4,3,1,8]))
