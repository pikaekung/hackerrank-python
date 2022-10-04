# BubbleSort.py

def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr

# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3


def countSwaps(a):
    # Write your code here
    s = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                s += 1
                swap(a, j, j+1)

    print("Array is sorted in {0} swaps.".format(s))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[len(a)-1]))
    return


n = 3
q = [3, 2, 1]
countSwaps(q)
