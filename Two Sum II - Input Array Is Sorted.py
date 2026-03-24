def Two_Sum_II(nums,target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return [left+1,right+1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

print(Two_Sum_II([2,7,11,15],9))

