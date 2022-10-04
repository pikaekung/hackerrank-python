
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(number):
        n = i + 1
        print("{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(n, w=width))


n = 99
print_formatted(n)
