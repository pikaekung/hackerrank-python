# arr = [7, 1, 3, 2, 4 ,5 ,6]
# i   arr                     swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took 5 swaps to sort the array.

# arr = [4, 3, 1, 2]
# i   arr            swap (indices)
# 0   [4, 3, 1, 2]   swap (0,2)
# 1   [1, 3, 4, 2]   swap (1,2)
# 2   [1, 4, 3, 2]   swap (1,3)
# 3   [1, 2, 3, 4]
# It took 3 swaps to sort the array.

# arr = [2, 3, 4, 1, 5]
# i   arr            swap (indices)
# 0   [2, 3, 4, 1, 5]   swap (0,2)
# ???
# It took 3 swaps to sort the array.


# q = [7, 1, 3, 2, 4, 5, 6]
# q = [4, 3, 1, 2]
# q = [1, 3, 5, 2, 4, 6, 7]
q = "2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19"
q = list(map(int, q.rstrip().split()))

# 6, 1, 3, 2, 4, 5, 7
# 1, 6, 3, 2, 4, 5, 7
# 1, 2, 3, 6, 4, 5, 7
# 1, 2, 3, 5, 4, 6, 7
# 1, 2, 3, 4, 5, 6, 7
# file = open('MinimumSwaps2-input.txt', 'r')
# K = int(file.readline())
# arr = file.readline()
# q = list(map(int, arr.rstrip().split()))


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


swap = 0
index = 0
for i in range(len(q)):
    # print(q[index], q[q[index]-1], end="")
    if q[index] != q[q[index]-1]:
        swap += 1
        q = swapPositions(q, index, q[index]-1)
        index = q[index]-1
    else:
        index += 1
    # print(" =>", q)

print(swap, q)

for i in range(30):
    if i+1 != q[i]:
        print(i+1, q[i])
