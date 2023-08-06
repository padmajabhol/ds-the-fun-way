def shuffle(nums, n):
    i = 0
    j = n
    res = []
    while(i < n):
        res.append(nums[i])
        res.append(nums[j])
        i += 1
        j += 1
    return res


print(shuffle([1,2,3,4,5,6,7,8], 4))
