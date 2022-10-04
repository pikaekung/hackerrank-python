# MarkAndToys.py
def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


def bubbleSortReverse(arr, k):
    sum = 0
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] < arr[j+1]:
                swap(arr, j, j+1)

        item = arr[len(arr)-1-i]
        sum += item
        count += 1
        print(item, sum, count)

        if sum > k:
            sum -= arr[len(arr)-1-i]
            count -= 1
            return count

    return count


def maximumToys(k, prices):
    return bubbleSortReverse(prices, k)


# k = 7
# s = "5 1 2 3 4"
# toys = list(map(int, s.split()))
FILE = open("MarkAndToys-input9.txt", "r")
line_1 = FILE.readline()
line_2 = FILE.readline()
k = int(line_1.split()[1])
toys = list(map(int, line_2.split()))

result = maximumToys(k, toys)
print(result)
