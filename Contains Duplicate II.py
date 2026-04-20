def ConatinsDuplicate(nums, k):
    empset = set()

    for i in range(len(nums)):
        
        if len(empset) > k:
            empset.remove(nums[i - k - 1])

        if nums[i] in empset:
            return True
        
        empset.add(nums[i])

    return False

print(ConatinsDuplicate([1,2,3,1,2,3], 2))