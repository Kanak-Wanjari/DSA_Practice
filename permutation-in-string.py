def pis(s1,s2):

    n = len(s1)
    m = len(s2)

    if n > m:
        return False
    
    count_1 = {}

    for i in range(n):
        count_1[s1[i]] = count_1.get(s1[i], 0) + 1

    for j in range(m - n + 1):
        count_2 = {}

        for k in range(j, j+n):
            count_2[s2[k]] = count_2.get(s2[k], 0) + 1

        if count_1 == count_2:
            return True
        
    return False

print(pis("ab","eidbaooo"))

    

    





























# s1 = "ab"
# s2 = "eidbaooo"

# n = len(s1)
# m = len(s2)

# if n>m:
#     print("String 1 is longer than String 2")


# count1 = {}
# for ch in s1:
#     count1[ch] = count1.get(ch,0) + 1

# for i in range(m-n+1):
#     window = s2[i:i+n]

#     count2 = {}
#     for ch in window:
#         count2[ch] = count2.get(ch,0) + 1

#     if count1 == count2:
#         print("True")
#         exit()

# print("False")