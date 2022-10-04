# SherlockAndAnagrams.py

s = "abba"

anag = 0
map = {}
for i in range(len(s)):
    for j in range(len(s) - i):
        s1 = ''.join(sorted(s[j:j + i + 1]))
        print(s1)
        # map[s1] = map.get(s1, 0) + 1

# print(map)

# for key in map:
#     print(key)
#     anag += (map[key] - 1) * map[key] // 2

# print(anag)


# i = 0,1,2,3
# j = -1,0,1,2
