def msodswlk(nums, k):
    w_sum = 0
    freq = {}
    max_sum = 0
    left = 0

    for right in range(len(nums)):
        w_sum += nums[right]
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        if right - left + 1 > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]

            w_sum -= nums[left]

            left += 1

    if right - left + 1 == k:
        if len(freq) == k:
            max_sum = max(max_sum, w_sum)

    return max_sum

print(msodswlk([4,4,4], 3))