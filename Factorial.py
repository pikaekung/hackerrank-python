
# 5! = 5x4x3x2x1
# 3! = 3x2x1
# 20! = 20x19x18x....x1

def recursiveFi(n):
    # print(n, "x")
    if n == 1:
        return n
    return n * recursiveFi(n-1)


def solve(n):
    return recursiveFi(n)


result = solve(10)
print(result)
