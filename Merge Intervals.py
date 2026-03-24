intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key = lambda x: x[0])

merged = []

for interval in intervals:
    if not merged:
        merged.append(interval)
    else:
        last = merged[-1]

        if interval[0] <= last[1]:
            last[1] = max(last[1], interval[1])
        else:
            merged.append(interval)

print(merged)