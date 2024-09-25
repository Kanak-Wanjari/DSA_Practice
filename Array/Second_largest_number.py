# arr = [12, 35, 35, 1, 10, 34, 1]

# max = arr[0]
# # second_max = 0
# for i in arr:
#     if i > max:
#         # second_max = max
#         max = i

# print(max)

# s_max = arr[0]

# for i in range(1,len(arr)):
#     if s_max!=max and s_max <arr[i]:
#         s_max = arr[i]
    
# print(s_max)

arr = [12, 35, 1, 10, 34, 1]

# Initialize max and second_max
max = float('-inf')
second_max = float('-inf')

for i in arr:
    if i > max:
        second_max = max
        max = i
    elif i > second_max and i != max:  # Check if i is the second max and not equal to max
        second_max = i

# Handle case where there's no second max
if second_max == float('-inf'):
    print("No second largest element found.")
else:
    print(second_max)