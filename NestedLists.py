

from unittest import result


scores = [['Harry', 37.21],
          ['Berry', 37.21],
          ['Tina', 37.2],
          ['Akriti', 41.0],
          ['Harsh', 39.0], ]

# scores = sorted(scores, key=lambda l: l[1])

result = []
scores.sort(key=lambda l: l[1])
minScore = scores[0][1]
minSecondScore = 0
for i in range(1, len(scores)):
    if scores[i][1] > minScore and minSecondScore == 0:
        minSecondScore = scores[i][1]
        # print("New second min score", minSecondScore)

    if (scores[i][1] == minSecondScore):
        result.append(scores[i])
        # print("Found", scores[i])

result.sort(key=lambda l: l[0])
print(result)
