def mergearray(arr1,arr2):

    mergedarr = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] <= arr2[j]:
                mergedarr.append(arr1[i])
            else:
                mergedarr.append(arr2[j])
    
    return mergedarr


arr1 = [10, 20, 30, 40]
arr2 = [15, 25, 35, 45, 50]

print(mergearray(arr1,arr2))