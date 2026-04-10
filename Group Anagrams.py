def groupAnagrams(strs):

    groups = {}

    for s in strs:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        key = tuple(sorted(count.items()))

        if key not in groups:
            groups[key] = []
        
        groups[key].append(s)

    return list(groups.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))






















# strs = ["eat","tea","tan","ate","nat","bat"]

# groups = {}

# for s in strs:
#     count = {}
    
#     for ch in s:
#         count[ch] = count.get(ch, 0) + 1
    
#     key = tuple(sorted(count.items()))

#     if key not in groups:
#         groups[key] = []
    
#     groups[key].append(s)

# print(list(groups.values()))