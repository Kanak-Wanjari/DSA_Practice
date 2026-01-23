a1 = [2,11,7,15]

target = 9

t1=0

for i in range(len(a1)):
    for j in range(i+1, len(a1)):
        t1=a1[i]+a1[j] 
        if t1 == target:
            print(i,j)