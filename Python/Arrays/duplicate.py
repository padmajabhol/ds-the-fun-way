def containsDuplicate(nums):
#   nums.sort()
#   length = len(nums)
#   for i in range(length - 1):
#       if nums[i] == nums[i+1]:
#           return True
#    return False
     hashset = set()
     for i in nums:
         if i in hashset:
             return True
         hashset.add(i)
     return False

print(containsDuplicate([2,14,18,22,22]))
