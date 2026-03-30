def mpycofc(cardpoints,k):

    left = 0
    right = len(cardpoints) - k

    total = sum(cardpoints[right:])

    res = total

    while right < len(cardpoints):
        total += (cardpoints[left] - cardpoints[right])
        res = max(res, total)
        left += 1
        right += 1
    
    return res

print(mpycofc([1,2,3,4,5,6,1],3))