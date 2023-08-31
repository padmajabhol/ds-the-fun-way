def min_heapify(A, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < len(A) and A[left] < A[smallest]:
        smallest = left
    else:
        smallest = i
    if right < len(A) and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        min_heapify(A, smallest)

def build_heapify(A):
    n = int((len(A)//2) - 1)
    for i in range(n, -1, -1):
        min_heapify(A, i)
    return A

print(build_heapify([2, 4, 11, 3, 6, 9]))

