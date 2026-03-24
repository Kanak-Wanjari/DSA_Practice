























# def valid_palindrome(s):

#     new_str = ""

#     for i in s:
#         if i.isalnum():
#             new_str += i.lower()
#     return new_str == new_str[::-1]






























# def valid_anagram(s, t):

#     freq1 = {}

#     for i in s:
#         if i in freq1:
#             freq1[i] += 1
#         else:
#             freq1[i] = 1
    
#     freq2 = {}

#     for j in t:
#         if j in freq2:
#             freq2[j] += 1
#         else:
#             freq2[j] = 1

#     if freq1 == freq2:
#         return True
#     else:
#         return False

# s = "anagram"
# t = "nagaram"

# print(valid_anagram(s, t))