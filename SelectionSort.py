
arr = [2, 5, 1, 3, 5, 2, 19, 3, 295, 2, 3, 1, 59, 9]


def solve(arr):
    print(arr)
    minIndex = 0
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    # endfor

    print(arr)


solve(arr)
