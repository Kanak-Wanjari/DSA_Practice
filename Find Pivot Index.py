def find_pivot_index(nums):

    total_sum = 0

    for i in range(len(nums)):
        total_sum = total_sum + nums[i]

    left_sum = 0

    for i in range(len(nums)):
        right_sum  = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        else:    
            left_sum = left_sum + nums[i]


num = [1,7,3,6,5,6]


print(find_pivot_index(num))
