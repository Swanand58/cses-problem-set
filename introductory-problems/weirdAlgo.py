
# Input:
# 3

# Output:
# 3 10 5 16 8 4 2 1

n = int(input())
finalList = []
finalList.append(n)
if n == 1:
    print(finalList[0])
    exit()

while True:
    if n % 2 == 0:
        n = n // 2
        finalList.append(n)
    else:
        n = 3 * n + 1
        finalList.append(n)

    if n == 1:
        break

for i in range(len(finalList)):
    print(finalList[i], end=" ")