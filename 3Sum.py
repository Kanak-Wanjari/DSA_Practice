def threesum(nums):
    res = []
    nums.sort()

    for i , a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        left = i+1
        right = len(nums) - 1

        while left < right:
            ts = a + nums[left] + nums[right]
            if ts > 0:
                right -= 1
            elif ts < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        
    return(res)

print(threesum([-1,0,1,2,-1,-4]))