arr = [7,1,5,3,6,4]

max_profit = 0
min_price = arr[0]

for i in range(1,len(arr)):
    if arr[i] < min_price:
        min_price = arr[i]
    else:
        profit = arr[i] - min_price
        if profit > max_profit:
            max_profit = profit

print(max_profit)