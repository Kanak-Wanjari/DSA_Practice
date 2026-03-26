def vp(str1):

    newstr = ""

    for i in str1:
        if i.isalnum():
            newstr += i.lower()
    return newstr == newstr[::-1]


print(vp("race a car"))