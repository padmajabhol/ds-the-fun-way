def reversearr(arr):
    def helper(start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        helper(start+1, end-1)
    helper(0, len(arr) - 1)
    return arr

def iterative(arr):
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1


    return arr

print(reversearr([1,2,3,4]))
print(iterative([1,3,5,7,9]))
