def tkfe(nums,k):

    freq = {}
    result = []

    for i in nums:
        freq[i] = freq.get(i,0) + 1

    sorted_items = sorted(freq.items(), key = lambda x:x[1], reverse = True)


    for i in range(k):
        result.append(sorted_items[i][0])

    return result

print(tkfe([1,1,1,2,2,3],2))























# nums = [1,1,1,2,2,1,3,3,3,3,3,3,]
# k = 2

# freq = {}

# for i in nums:
#     freq[i] =  freq.get(i,0) + 1

# sorted_items = sorted(freq.items(),key = lambda x:x[1], reverse = True)

# result = []

# for i in range(k):
#     result.append(sorted_items[i][0])

# print(result)