def mnoviasogl(s, k):

    if k > len(s):
        return 0

    vowels = {'a', 'e', 'i', 'o', 'u'}

    curr_count = 0
    max_count = 0

    for i in range(0,k):
        if s[i] in vowels:
            curr_count += 1

    max_count = curr_count

    for i in range(k,len(s)):
        if s[i-k] in vowels:
            curr_count -= 1

        if s[i] in vowels:
            curr_count += 1
        
        if curr_count > max_count:
            max_count = curr_count

        if max_count == k:
            return k
        
    return max_count

print(mnoviasogl("abciiidef",3))