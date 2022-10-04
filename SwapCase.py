s = "hG4 KIm2ONx3x5epersw Dz.ytOVfXSxrh'MephUyRYAkHsDZOZStP'2XRv6XqcT0RkI5INrfr38 4BPUuS85OGWXNgXZPaHF1oy"


def swap_case(s):
    ret = ""
    for i in range(len(s)):
        d = ord(s[i])
        # print(d, "(", s[i], ")", end=', ')
        if d >= 72 and d <= 90:
            ret += s[i].lower()
        elif d >= 97 and d <= 122:
            ret += s[i].upper()
        else:
            ret += s[i]
    return ret


print(swap_case(s))
