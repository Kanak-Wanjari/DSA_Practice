# nums = [0,8,2,6,7]
# target = 9

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         curr_sum = nums[i] + nums[j]
#         if curr_sum == target:
#             print(i,j)
#             break






# arr = [7,1,5,3,6,4]

# max_profit = 0
# min_price = arr[0]

# for i in range(len(arr)):
#     if arr[i] < min_price:
#         min_price = arr[i]
#     else:
#         profit = arr[i] - min_price
#         if profit > max_profit:
#             max_profit = profit

# print(max_profit)



arr =[-2,1,-3,4,-1,2,1,-5,4]

v1 = arr[0]
v2 = arr[0]

for i in range(1, len(arr)):
    if v1 + arr[i] > arr[i]:
        v1 = v1 + arr[i]
    else:
        v1 = arr[i]
    
    if v1>v2:
        v2 = v1

print(v2)


























