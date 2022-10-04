
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 1]
a, d = [1, 2, 3, 4, 5], 4


def solve(a, d):
    return a[d:len(a)] + a[0: d]


result = solve(a, d)
print(result)
