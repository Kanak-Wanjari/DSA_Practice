def mas(nums, k):
    curr_sum = 0

    for i in range(0,k):
        curr_sum += nums[i]

    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum = curr_sum - nums[i-k] + nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum/float(k)

print(mas([1,12,-5,-6,50,3],4))