from collections import Counter


def checkMagazine(magazine, note):
    # print(magazine, note)
    temp = note.copy()
    for i, v in enumerate(note):
        if v in magazine:
            del magazine[magazine.index(v)]
            del temp[temp.index(v)]

    if len(temp) == 0:
        return True

    return False

    # Ransom Note


def checkMagazineAnswer(magazine, note):
    # print(magazine, note)
    print(len(Counter(note) - Counter(magazine)) == 0)


M = list("two times three is not four".split())
N = list("two times two is four".split())
# FILE = open("RansomNote-input10.txt", 'r')
# l = FILE.readline()
# M = list(FILE.readline().split())
# N = list(FILE.readline().split())
# print(M, N)
result = checkMagazineAnswer(M, N)
print(result)
