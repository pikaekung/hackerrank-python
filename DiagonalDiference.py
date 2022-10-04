# DiagonalDiference.py

from turtle import right


n = 3
arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]

# left_diagonal = [0][0], [1][1], [2][2]
# right_diagonal = [0][2], [1][1], [2][0]

left_total = 0
right_total = 0
for i in range(n):
    left_total += arr[i][i]
    right_total += arr[i][(n-1)-i]

print(left_total, right_total)
print(abs(left_total - right_total))
