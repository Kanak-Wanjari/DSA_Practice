# Problem Name:- Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

def numOfSubarrays(nums, k, threshold):

    count = 0

    target = k * threshold
    
    window_sum = 0

    for i in range(0, k):
        window_sum += nums[i]

    if window_sum >= target:
        count += 1

    for i in range(k, len(nums)):
        window_sum -= nums[i - k]
        window_sum += nums[i]

        if window_sum >= target:
            count += 1

    return count

print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))