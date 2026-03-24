def movezeros(nums):

    i = 0

    while i < len(nums):
        if nums[i] != 0:
            i += 1
            continue

        j = i + 1

        while j < len(nums) and nums[j] == 0:
            j += 1

        if j == len(nums):
            break

        nums[i] , nums[j] = nums[j], nums[i]

    return(nums)


print(movezeros([0,1,0,3,12]))
























# nums = [0,1,0,3,12]

# i = 0

# while i < len(nums):
#     if nums[i] != 0:
#         i = i + 1
#         continue

#     j = i + 1

#     while j < len(nums) and nums[j] == 0:
#         j = j + 1
    
#     if j == len(nums):
#         break

#     nums[i] , nums[j] = nums[j] , nums[i]

#     i = i + 1

# print(nums)