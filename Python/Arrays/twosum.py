def twoSum(nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(twoSum([1, 2, 4, 8], 9))
