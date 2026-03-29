def msss(target, nums):

    left = 0
    curr_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    
    if min_length == float('inf'):
        return 0
    else:
        return min_length
    
print(msss(7,[2,3,1,2,4,3]))
    


























# nums = [2,3,1,2,4,3]
# target = 7

# left = 0
# current_sum = 0
# min_length = float('inf')

# for right in range(len(nums)):
#     current_sum = current_sum + nums[right]

#     while current_sum >= target:
#         min_length = min(min_length, right-left+1)
#         current_sum = current_sum - nums[left]
#         left = left + 1

# print(0 if min_length == float('inf') else min_length)