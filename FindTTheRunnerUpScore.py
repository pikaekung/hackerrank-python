
def solve(arr):
    arr.sort()
    arr.reverse()
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] < max:
            return arr[i]


n = 5
arr = [2, 3, 6, 6, 5]

print(solve(arr))
