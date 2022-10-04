input = "7 21"
input = list(map(int, input.split()))

N = input[0]
M = input[1]

# Top
for i in range(N//2):
    step = i+(i+1)
    print((".|."*step).center(M, "-"))

print("WELCOME".center(M, "-"))

# Bottom
for i in range(N//2, 0, -1):
    step = i+(i-1)
    print((".|."*step).center(M, "-"))
