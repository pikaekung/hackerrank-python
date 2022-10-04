
q = [[3, 1, 2],
     [2, 1, 5, 3, 4],
     [2, 5, 1, 3, 4],
     [5, 1, 2, 3, 7, 8, 6, 4],
     [1, 2, 5, 3, 7, 8, 6, 4]]


# 1,2,3,4,5,6,7,8
# B     1 1
# 1,2,5,3,4,6,7,8 => 2
# B         1
# 1,2,5,3,6,4,7,8 => 1
# B         1 1
# 1,2,5,3,7,6,4,8 => 2
# B           1 1
# 1,2,5,3,7,8,6,4 => 2

# 1,2,3,4,5,6,7,8
# 1,2,[5,3,7],8,6,4 => 2
# 1,2,5,3,[7,8,6],4 => 2
# 1,2,5,3,7,[8,6,4] => 2
# 1,2,5,3,7,8,[6,4] => 1

# 1,2,5,3,7,8,6,4
#

def blibe(q):
    rowCount = 0
    blibeCount = 0

    for i in range(len(q)-1):
        chaos = 0
        probler = 0
        for n in range(len(q)-1):
            rowCount += 1
            print(probler, chaos, q, rowCount)
            if q[n] > q[n+1]:
                if q[n] != probler:
                    probler = q[n]
                    chaos = 1
                else:
                    chaos += 1

                if chaos > 2:
                    return "Too chaotic"

                q[n], q[n+1] = q[n+1], q[n]
                blibeCount += 1

    return blibeCount


def solve(q):
    blibe = 0
    print(q)
    for i in range(len(q)):
        if q[i]-(i+1) > 2:
            print("Too chaotic")
            return

        # q[i] - 2 meaning start searching who blibe me. Why -2 because if your search x < -2 = too chaotic
        start = max(0, q[i]-2)
        for j in range(start, i):
            print(j, q[i], q[j], q[i] < q[j])
            if q[i] < q[j]:
                blibe += 1
    print(blibe)
    return


for n in range(len(q)):
    # O(n^2)
    # solve(q[n])
    solve(q[n])
