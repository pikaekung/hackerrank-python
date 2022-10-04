
s = "aba"
n = 10


def solve(s, n):
    lengthS = len(s)
    m = n - ((n // lengthS) * lengthS)
    ret = (aCount(s) * (n // lengthS)) + aCount(s[0:m])
    return ret


def aCount(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count += 1

    return count


#
print(solve(s, n))
