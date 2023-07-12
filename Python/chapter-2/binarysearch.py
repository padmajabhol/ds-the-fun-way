def binary_search(A, target):
    indexHigh = len(A) - 1
    indexLow = 0

    while indexLow <= indexHigh:
        mid = round((indexHigh + indexLow)/2)
        if A[mid] == target:
            return mid
        if A[mid] < target:
            indexLow = mid + 1
        else:
            indexHigh = mid - 1
    return -1

print(binary_search([1,3,4,5,6], 1))
