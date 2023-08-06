def sortColors(nums):
    l = len(nums)
    i = 1
    while(i < l):
        current = nums[i]
        j = i - 1
        while(j >= 0 and nums[j] > current):
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = current
        i = i + 1
    return nums

            
