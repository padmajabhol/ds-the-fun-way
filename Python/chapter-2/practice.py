def linear_Search(A, target):
    N = len(A)
    i = 0
    while i < N:
        if A[i] == target:
            return i
        i = i + 1
    return -1

def binary_search(A, target):
    high = len(A) - 1
    low = 0
    while low <= high:
        mid = round((high+low)/2)
        if A[mid] == target:
            return mid
        if A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
