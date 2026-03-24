s = "anagram"
t = "nagaram"

freq_1 = {}
freq_2 = {}

for ch in s:
    freq_1[ch] = freq_1.get(ch, 0) + 1

for ch in t:
    freq_2[ch] = freq_2.get(ch, 0) + 1

if freq_1 == freq_2:
    print(True)
else:
    print(False)