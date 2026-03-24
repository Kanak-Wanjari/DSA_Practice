def strStr(haystack,needle):
    
    n = len(haystack)
    m = len(needle)

    if needle == "":
        return 0
    
    for i in range(n - m + 1):
        match = True

        for j in range(m):
            if haystack[i+j] != needle[j]:
                match = False
                break

        if match == True:
            return i
        
    return -1

haystack = "Hello"
needle = "ll"

print(strStr(haystack,needle))