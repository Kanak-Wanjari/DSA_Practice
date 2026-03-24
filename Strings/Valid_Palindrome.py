def Valid_Palindrome(s):

    newstr = ""
    
    for i in s:
        if i.isalnum():
            newstr += i.lower()
        return newstr == newstr[::-1]
    
s = "A man, a plan, a canal: Panama"

print(Valid_Palindrome(s))