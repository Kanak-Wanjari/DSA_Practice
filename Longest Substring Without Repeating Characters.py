s = "abcabcbb"

if not s:
    print("0")
    
max_counter = 1

for i in range(len(s)):
    counter = 1
    for j in range(i+1, len(s)):
        if s[j] in s[i:j]:
            break
        else:
            counter = counter + 1
        if counter>max_counter:
            max_counter = counter
print(max_counter)