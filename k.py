prices = [10, 7, 1, 5, 3, 6, 4]

n = len(prices)
i = 0
max_profit = 0

while i < n - 1:

    # 1️⃣ Find local minimum (min_buy)
    while i < n - 1 and prices[i] >= prices[i + 1]:
        i += 1
    min_buy = prices[i]

    # 2️⃣ Find local maximum (max_sell)
    i += 1
    while i < n and prices[i] >= prices[i - 1]:
        i += 1
    max_sell = prices[i - 1]

    # 3️⃣ Calculate profit
    profit = max_sell - min_buy
    if profit > max_profit:
        max_profit = profit

print(max_profit)