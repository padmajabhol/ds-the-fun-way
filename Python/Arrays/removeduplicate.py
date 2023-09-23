def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1

print(removeDuplicates([1,1,2,2,3,3,3,4,4,4]))