def largestElement(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

print(largestElement([4,3,1,6,7,9,8]))