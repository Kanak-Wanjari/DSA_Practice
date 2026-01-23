nums = [-2,1,-3,4,-1,2,1,-5,4]

v1 = nums[0]
v2 = nums[0]

for i in range(1, len(nums)):
    if v1 + nums[i] > nums[i]:
        v1 = v1 + nums[i]
    else:
        v1 = nums[i]
    
    if v1>v2:
        v2 = v1

print(v2)




















# prices = [7,1,5,3,6,4]

# min_price = prices[0]
# max_profit = 0

# for i in range(len(prices)):
#     if prices[i] < min_price:
#         min_price = prices[i]
#     else:
#         profit = prices[i] - min_price
#         if profit > max_profit:
#             max_profit = profit
# print(max_profit)

# nums = [2,11,15,7,0]

# t1 = 9
# t2 = 0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         t2 = nums[i] + nums[j]
#         if t1 == t2:
#             print(i,j)