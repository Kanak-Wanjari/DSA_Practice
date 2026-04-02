def faaias(s,p):
    result = []

    if len(p) > len(s):
        return result

    p_freq = {}
    window_freq = {}

    for i in range(len(p)):
        p_freq[p[i]] = p_freq.get(p[i], 0 ) + 1
    
    left = 0

    for right in range(len(s)):
        window_freq[s[right]] = window_freq.get(s[right], 0) + 1

        if right - left + 1 > len(p):
            window_freq[s[left]] -= 1

            if window_freq[s[left]] == 0:
                del window_freq[s[left]]

            left += 1

        if right - left + 1 == len(p):
            if window_freq == p_freq:
                result.append(left)

    return result

print(faaias("cbaebabacd","abc"))