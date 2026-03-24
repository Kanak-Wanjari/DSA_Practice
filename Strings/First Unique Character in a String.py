def First_Unique_Character(s):
    
    freq = {}

    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for j in range(len(s)):
        ch = s[j]

        if freq[ch] == 1:
            return j
        
    return -1

s = "loveleetcode"

print(First_Unique_Character(s))