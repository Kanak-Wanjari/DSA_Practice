def missingno(nums):

    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i:
            return i
    
    return len(nums)

# missingno([3,0,4])

print(missingno([0,1,2,3,4]))