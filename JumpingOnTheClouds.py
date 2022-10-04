# Input
c = "0 0 0 1 0 0".split()
ret = 0
counter = 0

currentPosition = 0


def jumpForward(c, len, p):
    if p + 2 <= len and c[p + 2] != 1:
        p += 2
    elif p + 1 <= len and c[p + 1] != 1:
        p += 1

    return p


while currentPosition < len(c)-1:
    currentPosition = jumpForward(c, len(c)-1, currentPosition)
    ret += 1
    counter += 1

print(ret)
# print(currentPosition)
