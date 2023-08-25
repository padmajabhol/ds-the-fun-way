def sol(nums, k):
    mp = {}
    for i in range(k):
        if nums[i] in mp:
            mp[nums[i]] += 1
        else:
            mp[nums[i]] = 1
    max1 = max(mp, key=mp.get)
    min2 = min(mp, key=mp.get)
    print(max1, min2)

sol([10,5,10,15,10,5], 6)
