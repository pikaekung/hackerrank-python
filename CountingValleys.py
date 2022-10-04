# Input
steps = 8
path = "UDDDUDUU"

counter = 0
seaLv = 0
currentLv = 0
valleyCount = 0

for step in path:
    if step == "U":
        currentLv += 1
    elif step == "D":
        currentLv -= 1

    if currentLv == seaLv and step == "U":
        valleyCount += 1

print(valleyCount)
