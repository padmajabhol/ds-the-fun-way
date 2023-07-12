def compare_string(str1, str2):
    if len(str1) != len(str2):
        return False

    N = len(str1)
    i = 0
    while i < N and str1[i] == str2[i]:
        i = i + 1
    return i == N

#print(compare_string("mango", "mango")

def insert_sort(A):
    N = len(A)
    i = 1
    while i < N:
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = current
        i = i + 1

    return [0]

