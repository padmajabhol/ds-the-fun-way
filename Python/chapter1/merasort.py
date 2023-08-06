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

    return A

print(insertionSort([2,0,2,1,1,0]))
