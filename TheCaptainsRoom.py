

# K = 5
# arr = "1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2"
file = open('TheCaptainsRoom-Input5.txt', 'r')
K = int(file.readline())
arr = file.readline()


arr = list(map(int, arr.split()))
arr.sort()

value = arr[0]
count = 1
for i in range(1, len(arr)):
    temp = arr[i]
    if value == temp:
        count += 1
    else:
        if count < 10:
            print(value, count)
        count = 1
        value = temp
