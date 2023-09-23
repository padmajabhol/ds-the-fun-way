def majorityElements(nums):
    n = len(nums)
    m = {}
    for i in nums:
        if i in m.keys():
            m[i] += 1
        else:
            m[i] = 1

    n = n // 2
    for key, value in m.items():
        if value > n:
            return key

print(majorityElements([2,2,1,1,1,2,2]))
