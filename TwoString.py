from collections import Counter


def twoStrings(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    sum1 = sum(c1.values())
    sum2 = sum((c1 - c2).values())
    print(sum1, sum2)
    if sum1 - sum2 > 0:
        return "Yes"

    return "No"


arr = [["hello", "world"],
       ["hi", "world"]]

for i in range(len(arr)):
    result = twoStrings(arr[i][0], arr[i][1])
print(result)
