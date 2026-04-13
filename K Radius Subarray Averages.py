def krsa(nums, k):
    if k == 0:
        return nums
    
    n = len(nums)
    w_size = 2*k + 1
    
    if w_size > n:
        return [-1] * n
    
    res = [-1] * n
    w_sum = 0

    for i in range(w_size):
        w_sum += nums[i]

    res[k] = w_sum // w_size

    for i in range(w_size, n):
        w_sum += nums[i]
        w_sum -= nums[i - w_size]

        center = i - k
        res[center] = w_sum // w_size

    return res

print(krsa([7,4,3,9,1,8,5,2,6],3))