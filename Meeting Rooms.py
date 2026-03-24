intervals = [[5, 10], [15, 20]]

intervals.sort(key = lambda x:x[0])

can_attend = True

for i in range(1, len(intervals)):
    prev_end = intervals[i-1][1]
    curr_start = intervals[i][0]

    if curr_start < prev_end:
        can_attend = False
        break

print(can_attend)