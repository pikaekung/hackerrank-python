
pile = "42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42"
pile = pile.split()
pile.sort()
pairCount = 0
counter = 0
count = 0


for sock in pile:
    if counter == 0:
        pSock = sock
    else:
        if pSock != sock:
            pairCount += count // 2
            count = 0

        pSock = sock

    count += 1
    counter += 1

pairCount += count // 2
print(pairCount)
