arr =[-2,1,-3,4,-1,2,1,-5,4]        #[5,4,-1,7,8]

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