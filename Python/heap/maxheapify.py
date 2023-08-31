def max_heapify(A, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < len(A) and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right < len(A) and A[right] > A[i]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest] , A[i]
        max_heapify(A, largest)

def build_heapify(A):
    n = int((len(A)//2) - 1)
    for i in range(n , -1, -1):
        max_heapify(A, i)
    return A

A = [11, 6, 5, 0, 8, 2, 7]
print(build_heapify(A))




