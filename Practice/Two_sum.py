def twosum(nums,target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            t1 = nums[i] + nums[j]
            if t1 == target:
                return i,j
            
nums = [2,7,11,15]
target = 9

print(twosum(nums,target))