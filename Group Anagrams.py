strs = ["eat","tea","tan","ate","nat","bat"]

groups = {}

for s in strs:
    count = {}
    
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    key = tuple(sorted(count.items()))

    if key not in groups:
        groups[key] = []
    
    groups[key].append(s)

print(list(groups.values()))