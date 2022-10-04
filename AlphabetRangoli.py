def text(n, m):
    s = ""
    ascii_alphabet_start = 96
    for i in range(m, n, -1):
        s += chr(ascii_alphabet_start + i) + "-"

    s += chr(ascii_alphabet_start + n)

    for i in range(n+1, m+1):
        s += "-" + chr(ascii_alphabet_start + i)

    return s


def print_rangoli(size):
    # your code goes here
    thickness = ((size*2)-1) + ((size-1)*2)

    # TOP
    for i in range(size, 1, -1):
        print(text(i, size).center(thickness, "-"))

    # BOTTOM
    for i in range(1, size+1):
        print(text(i, size).center(thickness, "-"))

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
# ((size-1)**2)+1
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j


n = 5
print_rangoli(n)
