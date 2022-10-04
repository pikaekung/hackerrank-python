# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# print(arr)

# case 1
# [1 1 1 0 0 0]
# [0 1 0 0 0 0]
# [1 1 1 0 0 0]
# [0 0 2 4 4 0]
# [0 0 0 2 0 0]
# [0 0 1 2 4 0]

# arr = [[1, 1, 1, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [1, 1, 1, 0, 0, 0],
#        [0, 0, 2, 4, 4, 0],
#        [0, 0, 0, 2, 0, 0],
#        [0, 0, 1, 2, 4, 0]]

arr5 = [[-1, 1, -1, 0, 0, 0],
        [0, -1, 0, 0, 0, 0],
        [-1, -1, -1, 0, 0, 0],
        [0, -9, 2, -4, -4, 0],
        [-7, 0, 0, -2, 0, 0],
        [0, 0, -1, -2, -4, 0]]

# arr7 = [[0, -4, -6, 0, -7, -6],
#         [-1, -2, -6, -8, -3, -1],
#         [-8, -4, -2, -8, -8, -6],
#         [-3, -1, -2, -5, -7, -4],
#         [-3, -5, -3, -6, -6, -6],
#         [-3, -6, 0, -8, -6, -7]]


def solve(array):
    highest = None
    for i in range(4):
        for j in range(4):
            sum = 0
            sum = array[i][j] + array[i][j+1] + array[i][j+2]
            sum += array[i+1][j+1]
            sum += array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]

            if highest == None or sum > highest:
                highest = sum

    return highest


result = solve(arr5)
print(result)
